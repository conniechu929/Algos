# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        current = A
        while current.next is not None:
            runner = current.next
            while current.val == runner.val and runner.next is not None:
                runner = runner.next
            if current.val == runner.val and runner.next is None:
                current.next = None
            else:
                current.next = runner
                current = current.next
        return A
