# Solution 1 beats 98.75%
# Modifies the array in-place, O(n) time O(1) space
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if k == 0:
            return
        
        idx = len(nums)-k
        nums[:] = nums[idx:] + nums[:idx]