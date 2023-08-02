# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort nums arr in ascending order
        # keep track of current consecutive sequence counter
        # keep track of a maximum consec sequence counter
        # return maximum

        if len(nums) <= 1: return len(nums)

        nums = sorted(list(set(nums)))
        current_streak = 1
        max_streak = 1

        for idx in range(len(nums)):
            if (idx + 1) < len(nums) and (nums[idx] + 1) == nums[idx + 1]:
                current_streak += 1
            else:
                current_streak = 1
            
            if current_streak > max_streak:
                max_streak = current_streak


        return max_streak