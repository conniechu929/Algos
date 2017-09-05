# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current1 = l1
        current2 = l2
        current3 = head = runner = None

        while current1 or current2:
            if current1 is None or current2 is None:
                if current1 is None:
                    runner = current2
                    current2 = current2.next
                elif current2 is None:
                    runner = current1
                    current1 = current1.next

            elif current1.val <= current2.val:
                runner = current1
                current1 = current1.next
            elif current1.val > current2.val:
                runner = current2
                current2 = current2.next

            if head is None:
                head = runner
                current3 = head
            else:
                current3.next = runner
                current3 = current3.next

        return head
