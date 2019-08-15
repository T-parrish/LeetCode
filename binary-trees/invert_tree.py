# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def invertTree(self, root):
      """
      :type root: TreeNode
      :rtype: TreeNode
      """
      # recurse over tree, set left to right and right to left
      if root != None:
          root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
          return root