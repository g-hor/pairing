# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # loop over nums array in two directions: forwards and backwards
        # create an output array that is filled with ones so that any multiplication gives the same number
        # forward loop:
        #   > multiply output at the same idx by forward variable
        #   > multiply forward variable by the current num in input arr
        # backwards loop:
        #   > multiply output at the same idx by backwards variable
        #   > multiply backwards var by the current num in input arr

        lastIdx = len(nums) - 1
        fwd = 1
        back = 1
        output = [1 for i in range(len(nums))]

        for (idx, num) in enumerate(nums):
            output[idx] *= fwd
            fwd *= num
            
        for idx in range(lastIdx, -1, -1):
            output[idx] *= back
            back *= nums[idx]

        return output