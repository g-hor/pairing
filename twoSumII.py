# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two-pointer approach
        # left pointer starts at beginning of array
        # right pointer starts at end of array
        # both pointers progress towards the middle
        # if values at both pointers sum to target, return indices PLUS ONE (due to 1-indexed system)
        # if the sum is less than the target, our values are not great enough >> increment left pointer
        # if the sum is greater than target, our values are too great >> decrement right pointer

        left = 0
        right = len(numbers) - 1

        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum == target:
                return [left + 1, right + 1]
            elif currSum < target:
                left += 1
            else:
                right -= 1