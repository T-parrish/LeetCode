# Solution 1: beats 95%
# maps over array of integers to cast them as strings
# strings have access to the join method
# need to cast the new string as an int so we can add one
# since Ints aren't interable, we cast digits as a string
# them map it back into a list as an integer.
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = ''.join(map(str,digits))
        digits = int(digits) + 1
        digits = list(map(int, str(digits)))
        
        return digits

# Solution 2: beats 99%
# One-liner implementation of previous solution
# O(3n) -> O(n)time O(n) space
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
    
        return list(map(int,str((int(''.join(map(str, digits)))+1))))