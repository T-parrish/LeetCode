# Solution #1 beats 36%
# iterate through array, use dictionary as counter of values
# check array against dictionary to find the index 
# that only occurs once.
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for c in s:
            if c not in dict.keys():
                dict[c] = 1
            else:
                dict[c] += 1
        
        for idx in range(len(s)):
            if dict[s[idx]] == 1:
                return idx
        
        return -1