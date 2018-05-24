# Solution 1: beats 99.5%
# creates a dictionary -> number : count of occurrence
# pushes number from 2nd list into array and decrements
# the dictionary counter for each push 
# O(n) time complexity O(1) space
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict={}
        for num in nums1:
            if num not in dict:
                dict[num] = 1
            elif num in dict:
                dict[num] +=1
        
        res = []
        for num in nums2:
            if num in dict:
                res.append(num)
                value = dict[num]
                if value > 1:
                    dict[num]-=1
                else:
                    del dict[num]
            
        return res

# Solution 2: beats 36%
# simple solution, O(n^2) time and O(nLogn) space maybe slower
# removing the index from nums2 on each pass means you have
# to reassign indices to each value in the nums2 array 
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r=[]
        
        for i in nums1:
            if i in nums2:
                r.append(i)
                nums2.remove(i)
            
        return r