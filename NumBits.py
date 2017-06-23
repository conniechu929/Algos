# Write a function that takes an unsigned integer and returns the number of 1 bits it has.
#
# Example:
#
# The 32-bit integer 11 has binary representation
#
# 00000000000000000000000000001011
# so the function should return 3.

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        bit = '{0:32b}'.format(A)
        i = 0
        count = 0
        while i < len(bit):
            if bit[i] == '1':
                count += 1
            i += 1
        return count
