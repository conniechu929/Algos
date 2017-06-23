class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


def height(root):
    left_count = 0
    right_count = 0

    if root.left:
        left_count = 1 + height(root.left)
    if root.right:
        right_count = 1 + height(root.right)

    if left_count > right_count:
        return left_count
    else:
        return right_count
