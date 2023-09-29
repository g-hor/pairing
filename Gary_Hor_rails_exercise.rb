# Problems:
# 1. All UserEvents are queried, including ones outside of the date range we desire.
# 2. N+1 query to the database (one query to fetch users collection and 'N' additional 
#    queries where 'N' is the amount of user_events)
# 3. Since there are 10,000 users, memory usage can be intensive if processing all of 
#    them at once.
# 4. Excessive array methods that increase time and space complexity

# My approach:
# 1. Filter UserEvents by 'created_at' date range in the database rather than fetching 
#    all data and filtering using Ruby.
# 2. Eagerly load UserEvents by prefetching data using ::includes method
# 3. Use #find_each to process user_events in batches of 100 rather than all 
#    10,000 at once. This reduces memory usage because each user could potentially have
#    a large number of associated UserEvents.
# 4. Eliminate repetitive array iterations, such as #select and #sort_by, by presorting 
#    and filtering directly in the database


# Identify date range for data we desire (in this case, the current month)
start_range = Date.today.beginning_of_month
end_range = Date.today.end_of_month

# Initialize a hash map for users and the groups each respective user interacted with
distinct_groups = {}

# Query the database here. Filter, sort, and eagerly load to minimize operations/queries later on.
# Storing the entire Users collection to a variable would be memory intensive, so we iterate over
# this directly.
User
.where(role: role)
.joins(:user_events) # Use INNER_JOINS table for more efficient database query
.where('user_events.created_at >= ? AND user_events.created_at <= ?', start_range, end_range)
.order('user_events.created_at ASC')
.includes(:user_events) # Eager loading (N+1 buster)
.find_each(batch_size: 100) do |user| # Process 100 users at a time rather than all users at once
  user_name = nil
  last_event_time = nil
  total_time = 0
  
  # Initialize arrays that will hold information about the distinct groups for each event
  employers = []
  partners = []
  controller_resources = []

  user.user_events.each do |event|
    user_name = event.user_name 

    # Push names of employers and partners if the user had previously interacted with them before
    if event.last_known_session.present?
      employers << event.last_known_session["employer"]
      partners << event.last_known_session["partner"]
    end

    controller_resources << event.data["params"]["controller"]

    # Handles the case of first event and checks if at least 10 minutes have passed since the last event
    if last_event_time.nil? || (last_event_time + 10.minutes) < event.created_at
      # Except for the first event, add how much time has passed between current event and last event
      total_time += event.created_at - last_event_time unless last_event_time.nil?
      last_event_time = event.created_at
    end
  end

  distinct_groups[user_name] = {
    employers: employers,
    partners: partners,
    controller_resources: controller_resources,
    total_time: total_time
  }
end

# With my refactored code, 'distinct_groups' will contain usernames for keys. The values will be nested hash
# maps that contain the groups (in Array format) and 'total_time'. This information can be very useful for 
# tracking user engagement. 
# - If activities are expected to be relatively long (>= 10 min), the 'total_time' could be an indicator of 
#   how much time was spent using our system.
# - If activities are expected to be less than 10 min apart, then the 'total_time' indicates lapses in engagement.
# - We know which employers and partners the User interacted with the most, but using an Array data structure
#   also affords us a sense of progression, which may be useful in analyzing trends in navigation within our system.
# - Storing 'controller_resources' is useful for analyzing a User's interests. If this system is being used to 
#   track employee workflow, this can also be used to monitor proper performance. 


# Additional considerations:
# - Consider using OR-EQUALS assignment on line 63 if user_name cannot be altered to minimize reassignment.
# - Consider using a different data type, such as a hash map, for employers, partners, and controller_resources
#   for constant lookup time. I did not implement this because the front end may need access to the order of 
#   interactions. 