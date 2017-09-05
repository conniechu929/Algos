# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False
        else:
            count = []
            for i in range(len(s)):
                if s[i] == '(' or s[i] == '[' or s[i] == '{':
                    count += s[i]
                elif count:
                    if s[i] == ")" and count[-1] == '(' :
                        count.pop()
                    if s[i] == "]" and count[-1] == '[':
                        count.pop()
                    if s[i] == "}" and count[-1] == '{':
                        count.pop()

            if not count:
                return True
            else:
                return False




                
