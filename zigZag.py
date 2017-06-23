# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

# Return the zigzag version of the string

# My Solution:
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        pattern_str = ['' for i in range(len(s))]
        count = 0
        x = 1

        for i in s:
            pattern_str[count] += i
            count += x
            if count == 0 or count == numRows - 1:
                x = -x

        return "".join(pattern_str)
