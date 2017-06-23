# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        temp = []

        while current_node != None:
            temp.append(current_node.val)
            current_node = current_node.next

        # current = head
        for i in range(len(temp) - 1, -1, -1):
            current.val = temp[i]
            current = current.next
        return head
