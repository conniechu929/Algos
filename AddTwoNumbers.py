# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# My Solution:

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        value1 = value2 = ''
        # value2 = ''
        current1 = l1
        current2 = l2
        while current1 or current2:
            if current1:
                value1 = str(current1.val) + value1
                current1 = current1.next

        # while current2:
            if current2:
                value2 = str(current2.val) + value2
                current2 = current2.next

        total = str(int(value1) + int(value2))

        myNode = runner = ListNode(total[len(total)-1])

        # runner = myNode

        for i in range(len(total) - 2, - 1, -1):
            runner.next = ListNode(total[i])
            runner = runner.next

        return myNode


# Different solution:
class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
