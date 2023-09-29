# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two-pointer approach going in opposite directions towards the middle
        # Compare (lowercase) chars at both positions if alphanumeric
        # Return False early if not-matching
        # Return True if iterate successfully without returning early

        if s == "": return True

        alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'
        start = 0           # 1
        end = len(s) - 1    # 1

        while start < end:
            while s[start].lower() not in alphanumeric and start < end:
                start += 1
            while s[end].lower() not in alphanumeric and end > 0:
                end -= 1

            if s[start].lower() != s[end].lower() and s[start].lower() in alphanumeric and s[end].lower() in alphanumeric:
                return False

            start += 1
            end -= 1
        
        return True