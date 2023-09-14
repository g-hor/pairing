# 2396. Strictly Palindromic Number

# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

# Given an integer n, return true if n is strictly palindromic and false otherwise.

# A string is palindromic if it reads the same forward and backward.


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # for every case where we compare n to a base of (n - 2), the resulting string will be "12"
        # because "12" is not palindromic, we know there is no such value of n that will return True
        # therefore, we can return False

        return False