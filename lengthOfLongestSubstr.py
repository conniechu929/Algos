# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# My solution:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_dict = {}
        sub_str = ''
        max_length = 0

        for i in range(len(s)):
            if s[i] not in sub_str:
                sub_str = sub_str + s[i]
            else:
                sub_str = sub_str[sub_str.index(s[i])+1:] + s[i]
            # str_dict[len(sub_str)] = sub_str
            if max_length < len(sub_str):
                max_length = len(sub_str)

        # return max(str_dict) if str_dict else 0
        return max_length
