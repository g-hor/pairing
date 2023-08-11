# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:
        # upon hitting an open char, next char MUST be another open char OR a closing char of the SAME TYPE
        # iterate through the input string
        # use either string or array as a temporary holder
        # for each opening char, add the corresponding closing char to holder
        # if the current element is a closing char, it must be the same closing char at holder[-1]
        #   > if match, remove that closing char
        # if the holder is empty at the end, then return True
        # otherwise, return false


        closing_chars = []
        pair_chars = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in pair_chars:
                closing_chars.append(pair_chars[char])
            else:
                if closing_chars and closing_chars[-1] == char:
                    closing_chars.pop()
                else:
                    return False

        return len(closing_chars) == 0