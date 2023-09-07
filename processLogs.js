/*
Application logs are used in analysis of interactions with an application and may be used to detect specific actions. 

A log file is provided as a string array where each entry is in the form "user_id timestamp action". Each of the values is separated by a space. 
  - Both user_id and timestamp consist only of digits, are at most 9 digits long and start with a non-zero digit. 
  - timestamp represents the time in seconds since the application was last launched. 
  - action will be either "sign-in" or "sign-out"


Given a log with entries in no particular order, return an array of strings that denote user_id's of users who signed out in maxSpan seconds or less after signing in. 

Example:
n = 7
logs = ["30 99 sign-in", "30 105 sign-out", "12 100 sign-in", "20 80 sign-in", "12 120 sign-out", "20 101 sign-out", "21 110 sign-in"]
maxSpan = 20

The users with id's 30 and 12 were not signed in for more than maxSpan = 20 seconds. In sorted numerical order, the return array is ["12", "30"]

Function Description
Complete the function processLogs in the editor:
The function has the following parameter(s):
  - string logs[n]: each logs[i] denotes the ith entry in the logs. 
  - int maxSpan: the maximum difference in seconds between when a user logs in and logs out for the user to be included in the result. 

Returns: 
  - string[]: a string array of user id's sorted ascending by numeric value. 

Constraints:
   - 1 <= n, maxSpan <= 10^5
   - 1 <= maxSpan <= n 
   - Each user_id contains only characters in the range ascii['0'-'9'], is at most 9 digits long and starts with a non-zero digit. 
   - Each timestamp contains only characters in the range ascii['0'-'9'] and begins with a non-zero digit. 
   - 0 < timestamp <= 10^9
   - Each action is either "sign-in" or "sign-out"
   - Each user_id's sign-in timestamp < sign-out timestamp. 
   - Each user signs in for only 1 session. 
   - The result will contain at least one element. 
*/


// using a hash map (dictionary), keys will be user_ids and values will be:
//  > if key does not exist in hash yet, value as sign in time
//  > if key DOES exist, subtract sign in time from sign out time
//    - if this difference is less than or equal to maxSpan, we include that in our output array (as a string)

function processLogs(logs, maxSpan) {
  const shortSessions = [];
  const sessions = {};

  logs.forEach(entry => {
    const [userId, time, action] = entry.split(" ");
    if (!sessions[userId]) {
      sessions[userId] = Number(time);
    } else {
      const duration = Number(time) - sessions[userId]
      if (duration <= maxSpan) {
        shortSessions.push(userId)
      }
    }
  })

  return shortSessions.sort((a, b) => Number(a) - Number(b));
}


const logs = ["30 99 sign-in", "30 105 sign-out", "12 100 sign-in", "20 80 sign-in", "12 120 sign-out", "20 101 sign-out", "21 110 sign-in", "18 120 sign-in", "18 121 sign-out"];
maxSpan = 20; 

console.log(processLogs(logs, 20)) // ['12', '18', '30']