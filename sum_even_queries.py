# 985. Sum of Even Numbers After Queries

# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

# Return an integer array answer where answer[i] is the answer to the ith query.


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Create variable to keep track of current sum of all even numbers
        # To save space, update queries arr directly to contain desired current even sum
        # Iterate through nums array to determine current sum of even numbers
        # Iterate through queries array to perform desired additions.
        #   > for each potential change to nums array, check evenness of the sum:
        #       > update value
        #       > original: odd -> sum: even --->   add sum to total
        #       > original: odd -> sum: odd --->    only update value
        #       > original: even -> sum: even --->  add complement to total
        #       > original: even -> sum: odd --->   subtract original even num
        # return queries at the end

        curr_even_sum = 0

        for num in nums:
            if num % 2 == 0:
                curr_even_sum += num

        for query_idx,query in enumerate(queries):
            complement, idx = query
            total = nums[idx] + complement

            # if original number in nums arr is even
            if nums[idx] % 2 == 0:
                if total % 2 == 0:
                    curr_even_sum += complement
                else:
                    curr_even_sum -= nums[idx]
            # otherwise, original num is odd
            else:
                if total % 2 == 0:
                    curr_even_sum += total

            nums[idx] = total
            queries[query_idx] = curr_even_sum


        return queries