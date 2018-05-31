# Solution #1 beats 20%
# turns a dictionary into a counter
# checks second word against the dictionary by -1 the value
# for each time it occurs. If the dictionary values are not 
# all equal to 0 at the end, the words do not match.
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        tempDict = {}
        
        for l in s:
            if l not in tempDict:
                tempDict[l] = 1
            else:
                tempDict[l] += 1
        
        for l in t:
            if l not in tempDict:
                return False
            else:
                tempDict[l] -= 1
                
        for val in tempDict.values():
            if val != 0:
                return False
            
        return True
                