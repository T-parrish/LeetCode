# Solution 1: beats 99.8%
# turning a list into a set will remove all duplicates
# if the length of the set is less than the original array
# the original array must contain at minimum one duplicate value
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) > len(set(nums)):
            return True
        else:
            return False
        