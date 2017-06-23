# Write code to generate all possible case combinations of a given lower-cased string.
# example:
# "0ab" -> ["0ab", "0aB", "0Ab", "0AB"]

# my solution:

def permutate(string, left, index):
    if len(string) == len(left):
        return left
    else:
        if string[index].islower():
            permutate(string, left + string[index].upper(), index+1)
		permutate(string, left + string[index], index+1)

string = '0ab'
print permutate(string, '',0)
