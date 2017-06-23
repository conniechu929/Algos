# Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
#
# Example
#
# Input : 4
# Output : True
# as 2^2 = 4.


import math

class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 1:
            return True

        power = 0
        base = 2
        while base <= math.sqrt(A):
            power = int(math.log(A) / math.log(base))
            if power > 1 and math.pow(base, power) == A:
                return True
            base += 1

        return False
