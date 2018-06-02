# Solution 1 beats 99%
# simple sliding window solution, iterate through
# haystack by a window of size n, where n is the size
# of the needle. If the needle is bigger than the haystack,
# trigger the first edge case. If needle not found, return -1
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        
        if len(haystack) < n:
            return -1
        
        for i in range(len(haystack)-n + 1):
            if haystack[i:i+n] == needle[:]:
                return i

        return -1