# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        right_count = 1
        left_count = 1

        if root is None:
            return 0

        if root.right:
            right_count = 1 + self.maxDepth(root.right)
        if root.left:
            left_count = 1 + self.maxDepth(root.left)

        if right_count > left_count:
            return right_count
        else:
            return left_count

        
