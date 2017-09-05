# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0:
            return 0

        maxlength = 1
        start = 0
        for i in xrange(len(s)):
            if i-maxlength >= 1 and s[i-maxlength - 1: i+1] == s[i-maxlength - 1: i+1][::-1]:
                start = i - maxlength-1
                maxlength += 2
                continue
            if i-maxlength >= 0 and s[i-maxlength:i+1] == s[i-maxlength:i+1][::-1]:
                start = i-maxlength
                maxlength += 1
        return s[start:start+maxlength]