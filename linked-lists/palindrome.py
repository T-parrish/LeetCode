# Solution 1 : beats 100%
# Time: O(1) Space: O(n)

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        
        while head:
            stack.append(head.val)
            head = head.next
            
        return stack == stack[::-1]


# Solution 2: beats 100%
# Time: O(n) Space: O(1)
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # [head / p1 / p2]-> [n2] -> [n3]...
        p2 = p1 = head
        prev = None
        
        # If the list is empty, return true
        if not head:
            return True
    
        # Need to include p2.next for linked lists of size 1
        while p2.next and p2.next.next:
            # prev [head / p1] -> [n2] -> [p2]
            p2 = p2.next.next
            # prev [head / p1] -> [dummy] -> [p2]
            dummy = p1.next
            # prev <- [head / p1] -> [dummy] -> [p2]
            p1.next = prev
            # prev <- [head / prev / p1] -> [dummy] -> [p2]
            prev = p1
            # prev <- [head / prev] -> [dummy / p1] -> [p2]
            p1 = dummy
            
        # if even number of nodes
        if p2.next:
            # <- [head / prev] -> [p1 / dummy] ->[n3] -> [p2]
            p2 = p2.next
            # <- [head / prev] -> [p1] -> [dummy] -> [p2]
            dummy = p1.next
            # <- [head / prev] <- [p1] -> [dummy] -> [p2]
            p1.next = prev
            # <- [head] <- [prev/p1] -> [dummy] -> [p2]
            prev = p1
            # <- [head] <- [prev] -> [p1 / dummy] -> [p2]
            p1 = dummy
            
        # if odd number of nodes, set pointer forward one space from middle
        else:
            # [head] <- [n2] <- [prev] -> [dummy] -> [p1] -> [n6] -> [p2]
            p1 = p1.next
            
        while p1:
            if p1.val != prev.val:
                return False
            # [head] <- [prev] <- [n3] -> [dummy] -> [n5] -> [p1] -> [p2]
            prev = prev.next
            p1 = p1.next
            
        return True