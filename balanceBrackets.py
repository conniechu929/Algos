import sys

def parens(s):
    if len(s) % 2 != 0:
        return "NO"
    else:
        count = []
        balanced = True

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                count += s[i]
            else:
                if s[i] == ')':
                    if not count or count[-1] != '(':
                        balanced = False
                        break
                    else:
                        count.pop()
                elif s[i] == ']':
                    if not count or count[-1] != '[':
                        balanced = False
                        break
                    else:
                        count.pop()
                elif s[i] == '}':
                    if not count or count[-1] != '{':
                        balanced = False
                        break
                    else:
                        count.pop()

        if not count and balanced:
            return "YES"
        else:
            return 'NO'

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    print parens(s)
