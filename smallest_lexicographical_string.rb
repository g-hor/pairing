# 1663. Smallest String With A Given Numeric Value

# The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

# The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

# You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.


# create holder array to store letters
# use a loop to perform "n" operations from left to right of output:
#   - for each iteration of the loop, we add a letter to output array and subtract its value from the target total lexicographical value
#   - if the remaining spaces's combined value (k) exceeds or is equal to the maximum possible 26 per slot, then append "a" to output array
#   - otherwise, we are within the maximum limit of 26 per remaining slot, so we append the appropriate value 
#     by calculating the target value (k) subtracted by the amount of z's that can fit in remaining spots
# join output array to return string form

def get_smallest_string(n, k)
  output = []
  i = 0

  while i < n do
      if (n - i - 1) * 26 >= k
          output << "a"
          k -= 1
      else
          val = k - (n - i - 1) * 26
          output << (val + 96).chr
          k -= val
      end

      i += 1
  end


  return output.join('')
end