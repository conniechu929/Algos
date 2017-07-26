# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        stack = [(root, '')]
        visited = []
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                visited.append(value+str(node.val))
            if node.right:
                stack.append((node.right, value+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, value+str(node.val)+"->"))

        return visited
