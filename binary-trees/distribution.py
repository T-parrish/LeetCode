# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def distributeCoins(self, root):
      """
      :type root: TreeNode
      :rtype: int
      """
      self.acc = 0
      
      def dfs(node):
          if not node:
              return 0
          
          left_side = dfs(node.left)
          right_side = dfs(node.right)
          
          # accumulate totals of left side and right side
          # as we recurse over the tree
          self.acc += abs(left_side) + abs(right_side)
          # node value - 1 so that we get the surplus or deficiency 
          # from each node in the tree and roll it up into the parent node
          # if the node value is negative, it requires a coin and is accounted for
          # by grabbing the absolute value of each node as we recurse
          return node.val - 1 + left_side + right_side
          
      dfs(root)
      return self.acc