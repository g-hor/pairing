# 451. Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.


from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        chars = Counter(s)
        pairs = sorted(chars.items(), key=lambda pair:pair[1], reverse=True)
        output = ""

        for pair in pairs:
            output += (pair[0] * pair[1])

        return output