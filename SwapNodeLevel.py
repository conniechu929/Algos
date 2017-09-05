                
class Node(object):
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = Node(1)
        self.level = [self.root]
        self.current = self.root
        self.current_level = 0
        self.current_stack = []

    def create(self, str):
        temp = []
        while self.level:
        if len(self.level) > self.current_level:
            parent = self.level[self.current_level]
            if int(str[0]) != -1:
                parent.left = Node(int(str[0]))
                temp.append(parent.left)
            if int(str[1]) != -1:
                parent.right = Node(int(str[1]))
                temp.append(parent.right)
            self.current_level += 1
            self.current_stack.extend(temp)
        else:
            parent = self.level[0]
            if int(str[0]) != -1:
                self.current.left = Node(int(str[0]))
                temp.append(self.current.left)
            if int(str[1]) != -1:
                self.current.right = Node(int(str[1]))
                temp.append(self.current.right)
            self.current_level = 1
            self.current_stack.extend(temp)


def swapEveryKLevelUtil(root, level, k):
    if (root is None or (root.left is None and
                        root.right is None ) ):
        return

    if (level+1)%k == 0:
        root.left, root.right = root.right, root.left

    swapEveryKLevelUtil(root.left, level+1, k)
    swapEveryKLevelUtil(root.right, level+1, k)

def swapEveryKLevel(root, k):
    swapEveryKLevelUtil(root, 1, k)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)



tree = BinarySearchTree()
t = int(raw_input())
for n in range(t):
    str = raw_input().split()
    tree.create(str)
