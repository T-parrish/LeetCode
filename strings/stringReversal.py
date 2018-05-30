# Solution 1 beats 83.67%
# Simple string reversal - takes a string
# and returns the whole thing -1 position at a time
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

