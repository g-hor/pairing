# Background:
# The following code works but I have intentionally introduced issues to make it inefficient.
# UserEvents are created for every interaction a user has in the system. It stores what employer, partner and 
# controller they were on. When there were 10 users and only a little bit of traffic, this would run quickly.
# But now with 10,000 users and months of traffic - (millions of user events), this code would be very inefficient.

# Instructions:
# 1. Please make this code more efficient through refactoring so that it can run at a greater scale, 
#    along with adding some comments to improve the readability.
# 2. Please explain what the variable 'distinct_groups' will contain by the end of the execution and what
#    this data would be useful for.
# 3. Send the resulting file as a gist, .rb file or zip package via email to ryan@zevobenefits.com



# Problems:
# 1. All UserEvents are queried, including ones outside of the date range we desire.
# 2. N+1 query to the database (one query to fetch users collection and 'N' additional 
#    queries where 'N' is the amount of user_events)
# 3. Since there are 10,000 users, memory usage can be intensive if processing all of 
#    them at once.
# 4. Excessive array methods that increase time and space complexity

# My solutions:
# 1. Filter UserEvents by 'created_at' date range in the database rather than fetching 
#    all data and filtering using Ruby.
# 2. Eagerly load UserEvents by prefetching data using ::includes method
# 3. Use #find_each to process user_events in batches of 100 rather than all 
#    10,000 at once. This reduces memory usage because each user could potentially have
#    a large number of associated UserEvents.
# 4. Eliminate repetitive array iterations, such as #select and #sort_by, by presorting 
#    and filtering directly in the database



# Identify date range for data we desire
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


# Additional considerations:
# - Consider using OR-EQUALS assignment on line 63 if user_name cannot be altered to minimize reassignment.
# - Consider using a different data type, such as a hash map, for employers, partners, and controller_resources
#   for constant lookup time. I did not implement this because the front end may need access to the order of 
#   interactions. 