# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # iterate through nums array in reverse order
        # upon reaching a '0'
        #   > check nums after the '0' to see if any number can jump past the '0'

        if len(nums) == 1: return True
        if nums[0] == 0: return False

        difference = 0

        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] == 0:
                idx -= 1
                difference = 1

                while nums[idx] <= difference:
                    idx -= 1
                    difference += 1
                    if idx <= -1:
                        return False


        return True


        # DP: O(n^2) approach

        # memo = {}
        # idx = 0

        # def _jump(nums, memo, idx):
        #     if idx >= len(nums) - 1: return True
        #     if idx in memo: return memo[idx]

        #     for i in range(1, nums[idx] + 1):
        #         if _jump(nums, memo, idx + i):
        #             memo[idx] = True
        #             return True

        #     memo[idx] = False
        #     return False

        # return _jump(nums, memo, idx)