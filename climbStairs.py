# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



class Solution:
    def climbStairs(self, n: int) -> int:
        # base case: return 1 if n is 1
        # base case: return 2 if n is 2
        # for each recursive step, if there are two steps to be made,
        #   > either 1 + 1
        #   > or 2
        # add result of next call stack
        memo = {}

        def helpStep(n, memo):
            if n == 1: return 1
            if n == 2: return 2
            if n in memo: return memo[n]

            memo[n] = helpStep((n - 1), memo) + helpStep((n - 2), memo)
            return memo[n]

        return helpStep(n, memo)