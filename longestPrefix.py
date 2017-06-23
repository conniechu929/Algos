# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # i = 0
        # j = 1

        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""
        else:
            prefix = "" + strs[0]
            for i in range(1, len(strs)):
                while strs[i][:len(prefix)] != prefix and prefix:
                    prefix = prefix[:len(prefix)-1]
            return prefix
