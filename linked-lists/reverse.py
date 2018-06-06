# Solution 1: beats 99.6%
# Time: O(1) Space: O(1)
# Iterative solution
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # No data before the head
        previous = None
        
        while head:
            # None -> [curr / head] -> [2] -> [3]
            curr = head
            # None -> [curr] -> [head] -> [3]
            head = head.next
            # None <- [curr] -> [head] -> [3]
            curr.next = previous
            # None <- [curr/ previous] -> [head] -> [3]
            previous = curr
            
        # Returns the Linked List starting from the tail
        return previous