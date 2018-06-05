# Solution #1 - 
# Modifies the linked list such that 
# the pointer changes from current node (node.val) 
# to the node after (node.val.next) and the
# next node (node.next) to the one after that -> node.next.next
# Space : O(1) Time: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next