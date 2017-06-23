# Input: {WWWB} , K = 2
# Output: 0
#
# Explanation:
# We have 3 choices {W, WWB}, {WW, WB}, {WWW, B}
# for first choice we will get 1*0 + 2*1 = 2.
# for second choice we will get 2*0 + 1*1 = 1.
# for third choice we will get 3*0 + 0*1 = 0.
#
# Of the 3 choices, the third choice is the best option.

def arrange(self, A, B):
    if len(A) < 2:
        return -1
    else:
        stables = {}
        i = 0
        for letter, stable in enumerate(A):
            if letter not in stables:
