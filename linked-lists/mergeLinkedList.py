# Solution #1 beats 76%
# Time: O(nlogn) Space: O(n)
# pretty sure that the time is O(nlogn) because of the sort method

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 is empty, return l2
        if not l1:
            return l2
        # if l2 is empty, return l1
        if not l2: 
            return l1
        
        container = []
        
        # push all l1 node values into container 
        while l1:
            container.append(l1.val)
            l1 = l1.next
        # push all l2 node values into container
        while l2:
            container.append(l2.val)
            l2 = l2.next
        
        # sort the container
        container.sort()
        
        # -> [l3 / head]
        l3 = head = ListNode(container[0])
        for i in range(1, len(container)):
            # -> [l3 / head / 1 / container[0]] -> [container[1]]
            head.next = ListNode(container[i])
            # -> [l3 / 1 / container[0]] -> [head / container[1]]
            head = head.next
            
        return l3


# Solution #2  beats 97%
# Time: O(n) Space: O(1)
# Using pointers to win the day

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 is empty, return l2
        if not l1:
            return l2
        # if l2 is empty, return l1
        if not l2:
            return l1
        
        # l3/head/None exists before the first ndoe
        l3 = head = ListNode(None)
        # while l1 and l2 both return true
        while l1 and l2:
            if l1.val <= l2.val:
                # head / l3 -> [l1]
                l3.next = l1
                # -> [l1.prev] -> [l1]
                l1 = l1.next
            else:
                # head / l3 -> [l2]
                l3.next = l2
                # -> [l2.prev] -> [l2]
                l2 = l2.next
                
            # head -> [l1 || l2 / l3]
            l3 = l3.next
            
        # if the while block finishes l2 before l1,
        # head -> [l1 || l2] -> [l1 || l2] -> [l2] - > [l3.next / l1]
        if l1 :
            l3.next = l1
        # if the while block finishes l1 before l2,
        # head -> [l1 || l2] -> [l1 || l2] -> [l1] - > [l3.next / l2]
        if l2 :
            l3.next = l2
            
        
        return head.next
                
# Solution #1 beats 96%
# Time: (1) Space: (2^n) since it's a recursive algorithm
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else: 
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2