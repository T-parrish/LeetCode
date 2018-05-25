# Solution 1: beats 10%
# straightforward solution, not optimal
# O(n) space O(n^2) time because removing the zeroes from non-ending 
# positions results in an automatic re-index of all array values
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)

# Solution 2: beats 92%
# More efficient because it modifies multiple indices of the array
# Simultaneously in place rather than iteratively. This removes the need
# To reindex the array values for each pass and optimizes the algorithm.
# O(n) space, O(n) time complexity
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        for num in nums:
            if num==0:
                zeroes+=1
                
        if len(nums) == 1:
            nums[:] = nums[:]
        if 0 not in nums[:]:
            nums[:] = nums[:]
        else:
            nums[:-zeroes] = [num for num in nums if num != 0]
            nums[-zeroes:] = [0 for i in range(zeroes)]