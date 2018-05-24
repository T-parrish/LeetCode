# Solution 1: beats 22%
# If you sum a set and subtract the sum of the original list
# You'll be left with the number that only appears once
# 2*(a + b + c) - (a + a + b + c + c) = b

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return 2*sum(set(nums))-sum(nums)

# Solution 2: beats 47.6%
# iterate through list, can only pop keys that already exist
# if key doesn't exist, set dict{num:1} and continue iterating
# by end of iteration, there should only be one key:value
# return the key with popitem[0]
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict = {}
        for num in nums:
            try:
                dict.pop(num)
            except:
                dict[num] = 1
            
        return dict.popitem()[0]

# Solution 3 : beats 95%
# Creates and XOR gate 
# a XOR a = 0 a XOR 0 = a
# reduces to (a XOR a) XOR b = (0 XOR b) = b
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = 0
        for i in nums:
            a ^= i
        return a