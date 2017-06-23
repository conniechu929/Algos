class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def insert(self, val):
        if self.val == val:
            return False
        elif self.val > val:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = Node(val)
                return True
        else:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = Node(val)
                return True

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

def DFS_present(tree, target):
    if tree.root == None:
        return False

    visited, stack = list(), [tree.root]
    while stack:
        item = stack.pop()
        visted.append(item)
        if item.val == target:
            return True
        else:
            stack.extend(filter(None, [item.right, item.left]))
    return False

def DFS_tree(tree):
    if tree.root == None:
        return []

    visited, stack = list(), [tree.root]
    while stack:
        item = stack.pop()
        visited.append(item)
        stack.extend(filter(None, [item.right, item.left]))
    return visited

def BFS_tree(tree):
    if tree.root == None:
        return []

    visited, queue = list(), [tree.root]
    while queue:
        item = queue.pop(0)
        visited.add(item)
        queue.extend(filter(None, [item.left, item.right]))
    return visited
