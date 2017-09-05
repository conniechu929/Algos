# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right, result = n, n, []
        self.dfs(left, right, result, '')
        return result

    def dfs(self, left, right, result, string):
        if right < left:
            return
        if not left and not right:
            result.append(string)
            return result
        if left:
            self.dfs(left-1, right, result, string + "(")
        if right:
            self.dfs(left, right-1, result, string + ')')
