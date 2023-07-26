# 1877. Minimize Maximum Pair Sum in Array

# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.



# sort the array of nums in ascending/descending order
# iterate thru sorted arr and find pair sums based on complementary index (length - index)
# keep track of maximum pair sum while iterating and return max

def min_pair_sum(nums)
  nums.sort!

  length = nums.length
  max_pair = nums[0] + nums[-1]
  half_point = length/2 - 1
  index = 1

  while (index <= half_point) do
      current_pair = nums[index] + nums[length - index - 1]
      max_pair = current_pair if current_pair > max_pair
      index += 1
  end

  max_pair
end