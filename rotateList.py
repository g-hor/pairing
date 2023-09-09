# 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # reassign k to be the result of k modded by length of array
        # reverse the nums array
        # iterate over the reversed array:
        #   > "partition" array into two sections:
        #       > first section is length k
        #           > starting from index 0..k-1, swap the complementary index
        #           > e.g. when k is 3, 0 swaps with 2, and 1 swaps with 1
        #       > second section is the remainder of the array
        #           > starting from index k..length - 1, swap complementary index

        length = len(nums)

        k = k % length 

        reversed_nums = []
        for idx in range((length - 1), -1, -1):
            reversed_nums.append(nums[idx])

        for idx in range((k - 1), -1, -1):
            nums[k - 1 - idx] = reversed_nums[idx]

        for idx in range((length - 1), (k - 1), -1):
            nums[k + length - 1 - idx] = reversed_nums[idx]
        