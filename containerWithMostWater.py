# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maximumWater = 0
        length = len(height)
        start = 0
        end = length - 1

        while start < end:
            width = end - start
            currentWater = min(height[end], height[start]) * width
            maximumWater = max(maximumWater, currentWater)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return maximumWater