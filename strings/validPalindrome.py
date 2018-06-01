# Solution 1 beats 99%
# Regex is fastest way to filter out punctuation and stuff since 3.6
# [\W]+ -> greedy matcher, matches every non-word character
# substitute every non-word character with '' and make everything lowercase
# since this also strips the space away, if the string is 
# the same backwards as forwards, it returns true otherwise false. 

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        import re
        
        pattern = re.compile('[\W]+')
        s = pattern.sub('', s).lower()
        
        return s[::-1] == s[:]