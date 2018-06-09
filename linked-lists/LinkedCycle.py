# Solution #1 beats 33%
# Time: O(1) Space: O(n)
# uses a set to check if the linked list is repeating itself
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

# Solution #2 beats 19%
# Time : O(n) Space : O(1)
# Pointers comb through the linked list to find a cycle

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = p2 = head
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True
            
        return False
    
