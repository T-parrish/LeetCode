# First solution - beats 46% of others

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] == nums[i-1]:
                del nums[i]


# Solution two: beats 76%
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        idx = 0
        j = 0
        
        if len(nums) == 0:
            return 0
        
        while j < len(nums):
            if nums[j] != nums[idx]:
                idx += 1
                nums[idx] = nums[j]
            j+= 1

                
        return idx + 1 