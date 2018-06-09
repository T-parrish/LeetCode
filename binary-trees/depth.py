# Solution #1 beats 99%
# Time : O(n) Space : O(n) 
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0

        queue = [root]
        depth = 0

        while queue:
            depth += 1
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp

        return depth

# Solution #2 beats 22%
# Time : O(2^n) Space : O(1)
# recursive solution, adds one each time the 
# maxDepth function is called
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        else: 
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1