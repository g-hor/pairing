# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# SETUP:
# create a start array containing all beginning points of each interval
# create an end array for endpoints of intervals
# iterate through intervals 2d arr:
#   > append startpoints (interval[0]) 
#   > append endpoints (interval[1])
# sort startpoints and endpoints in ascending order

# RESULT:
# create a holder output array
# use loop to go through starting and ending points arrays:
#   > check if current starting index + 1 is within range of endpoint at current start idx
#       > then we CAN merge, but we should keep looking in case of more overlaps
#       > once we no longer find an overlap, append the final overlapping pair to output array

# return output array


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        start = []
        end = []
        output = []
        
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        
        start.sort()
        end.sort()

        start_index = 0
        end_index = 0

        while start_index < len(start) and end_index < len(end):
            while end_index != len(end) - 1 and start[end_index + 1] <= end[end_index]:
                end_index += 1
            
            output.append([start[start_index], end[end_index]])
            end_index += 1
            start_index = end_index

        return output