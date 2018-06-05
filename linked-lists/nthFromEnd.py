# Solution #1 beats 96%
# Optimizes for time over space
# Time: O(1) Space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # store values in list for constant time access
        as_list = []
        node = head
        
        # for each node starting from head, append the value to as_list
        # set the node value to the next node, and repeat until done
        while node:
            as_list.append(node)
            node = node.next
            
        # Calculate index of linked list by taking the length of the list
        # and subtracting the 'n' term to figure out what needs to be removed
        diff = len(as_list) - n
        
        # If the length of the linked list minus n = 0,
        # That means the head is the one that needs to change
        if diff == 0:
            head = head.next
        else:
            # Change the pointer from the nth term from the end to the one after
            as_list[diff-1].next = as_list[diff].next
        
        # return the head
        return head