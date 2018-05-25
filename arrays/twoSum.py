# Solution 1: beats 13%
# Brute force the solution with I and J, ensure that J 
# always starts + 1 index from I so you don't add the same index.
# O(1) space O(n^2) time
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]

# Solution 2: beats 36%
# Creates a dictionary to store idx and value
# subtract value iteratively from temp and check rest of dictionary
# to see if the remainder exists. returns the indices of the values.
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashDict = dict(enumerate(nums))
        
        for k, v in hashDict.items():
            temp = target - v
            if(temp in hashDict.values() and list(hashDict.values()).index(temp) != k):
                return sorted([list(hashDict.values()).index(temp),k])