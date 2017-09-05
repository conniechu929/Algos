# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        result, level = [], []

        while True:
            while root:
                level.append(root)
                root = root.left
            if not level:
                return result
            node = level.pop()
            result.append(node.val)
            root = node.right
