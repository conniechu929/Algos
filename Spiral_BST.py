class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if root == None:
            return []

        result, temp, queue, flag = list(), list(), [root], 1
        while queue:
            for i in xrange(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp[::flag])
            temp = []
            flag *= -1
        return result
