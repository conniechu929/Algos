# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return []

        result = []

        for i in lists:
            while i:
                result.append(i.val)
                i = i.next

        return sorted(result)




from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return []

        my_node = current = ListNode(None)

        result = PriorityQueue()

        for i in lists:
            if i:
                result.put((i.val, i))

        while result.qsize() > 0:
            current.next = result.get()[1]
            current = current.next
            if current.next:
                result.put((current.next.val, current.next))
        return my_node.next
