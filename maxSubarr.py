# 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSum = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0 and num > currSum:
                currSum = 0

            currSum += num
            
            if currSum > maxSum:
                maxSum = currSum
            

        return maxSum