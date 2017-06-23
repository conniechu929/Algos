class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def printKDistance(root, k):
    if root is None:
        return
    if k == 0:
        print root.val
        return
    else:
        printKDistance(root.left, k-1)
        printKDistance(root.right, k-1)

def printKDistanceNodeDown(root, k):
    if root is None or k < 0:
        return
    if k == 0:
        print root.val
        return
    printKDistanceNodeDown(root.left, k-1)
    printKDistanceNodeDown(root.right, k-1)

def printKDistanceNode(root, target, k):
    if root is None:
        return -1

    if root == target:
        printKDistanceNodeDown(root, k)
        return 0

    dL = printKDistanceNode(root.left, target, k)

    if dL != -1:
        if dL + 1 == k:
            print root.val
        else:
            printKDistanceNodeDown(root.right, k - dL - 2)
        return 1 + dL

    dR = printKDistanceNode(root.right, target, k)

    if dR != -1:
        if dR + 1 == k:
            print root.val
        else:
            printKDistanceNodeDown(root.left, k - dR - 2)
        return 1 + dR

    return -1
