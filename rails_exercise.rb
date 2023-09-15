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
# 2. N+1 query to the database (one query to fetch users collection and 'N' additional queries where 'N' is the amount of user_events)
# 3. Since there are 10,000 users, memory usage can be intensive if processing all of them at once.
# 4. Excessive array methods that increase time and space complexity

# My solutions:
# 1. Filter UserEvents by 'created_at' date range in the database rather than fetching all data and filtering using Ruby.
# 2. Eagerly load UserEvents by prefetching data using ::includes method
# 3. Use #find_in_batches to process user_events in batches of 1000 rather than all 10,000 at once.
# 4. Eliminate repetitive array iterations, such as #select and #sort_by, by presorting and filtering directly in the database


# Identify date range for data we desire
start_range = Date.today.beginning_of_month
end_range = Date.today.end_of_month

# Using an INNER_JOIN table, combine and query relevant information 
# Filter only users where there are UserEvents in desired date range
# Order our data in ascending order
# This way, we only retrieve necessary information and eliminate the need to perform resource-consuming iterative methods.
users = User
  .where(role: role)
  .joins(:user_events)
  .where('user_events.created_at >= ? AND user_events.created_at <= ?', start_range, end_range)
  .order('user_events.created_at ASC')
  .includes(:user_events) # Eager loading (N+1)


employers = []
partners = []
controller_resources = []

distinct_groups = {}

users.each do |user|
  time = 0
  last_time = nil
  times = []
  user_name = nil

  user.user_events.each do |event|
    user_name = event.user_name
    if event.last_known_session.present?
      employers << event.last_known_session["employer"]
      partners << event.last_known_session["partner"]
    end
    controller_resources << event.data["params"]["controller"]
    if last_time.nil? || last_time+10.minutes < event.created_at
      times << time
      time = 0
      last_time = event.created_at
    else
      time += event.created_at - last_time
      last_time = event.created_at
    end
  end

  times << time
  sum = times.reduce(:+)
  distinct_groups[user_name] = sum
end
