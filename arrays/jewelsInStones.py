# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# O(n) time, O(n) space
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        dict = {}
        for i in range(len(S)):
            if S[i] not in dict.keys():
                dict[S[i]] = 1
            else:
                dict[S[i]] += 1
        
        for j in range(len(J)):
            if J[j] in dict.keys():
                counter += dict[J[j]]
            
        return counter

# O(n^2) time, O(n) space
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([i in J for i in S])
            