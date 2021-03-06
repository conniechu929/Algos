# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = []

        new_string = s.split(" ")

        for i in range(len(new_string)):
            result.append(new_string[i][::-1])

        return ' '.join(result)
