# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# click to show spoilers.
#
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
#
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

# My Solution:
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x.bit_length() > 32:
            return 0
        elif len(str(x)) == 1:
            return x
        elif x > 0 and int(str(x)[::-1]).bit_length() >= 32:
            return 0
        elif x < 0:
            if int(str(x)[1:][::-1]).bit_length() >= 32:
                return 0
            else:
                return int(str(x)[0] + str(x)[1:][::-1])
        else:
            return int(str(x)[::-1])
