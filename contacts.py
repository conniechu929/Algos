class Trie(object):
    __slots__ = ('my_dict', 'count')
    def __init__(self):
        self.my_dict = {}
        self.count = 0

def add(trie, word):
    current_dict = trie

    for letter in word:
        if letter not in current_dict.my_dict:
            current_dict.my_dict[letter] = Trie()
        current_dict = current_dict.my_dict[letter]
        current_dict.count += 1

def find_partial(trie, string):
    current_dict = trie
    for letter in string:
        if letter not in current_dict.my_dict:
            return 0
        current_dict = current_dict.my_dict[letter]

    return current_dict.count


t = int(raw_input())
trie = Trie()
for i in range(t):
    s = raw_input().split()
    if s[0] == "add":
        add(trie, s[1])
    else:
        print find_partial(trie, s[1])

# -------------------------------------------------------------------------------------

contacts = {}

def add(name):
    for i in range(1, len(name)+1):
        if name[:i] in contacts:
            contacts[name[:i]] += 1
        else:
            contacts[name[:i]] = 1

def find_partial(partial):
    return contacts.get(partial) or 0


t = int(raw_input())
for i in range(t):
    s = raw_input().split()
    if s[0] == "add":
        add(s[1])
    else:
        print find_partial(s[1])

# -------------------------------------------------------------------------------------
# all letters, a, ab, abc, ..
def edge_ngram(contact):
    return [contact[0:idx] for idx in range(1, len(contact) + 1)]

contact_indices = {}
def add(contact):
    for token in edge_ngram(contact):
        contact_indices[token] =contact_indices.get(token, 0) + 1

def find(name):
    return contact_indices.get(name, 0)

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add(contact)
    elif op == 'find':
        print(find(contact))
