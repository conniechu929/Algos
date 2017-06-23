# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        n = len(matrix[0])
        low, high = 0, len(matrix) * n

        while low < high:
            middle = (low + high) / 2
            i = matrix[middle/n][middle%n]

            if i < target:
                low = middle + 1
            elif i > target:
                high = middle
            else:
                return True
        return False
