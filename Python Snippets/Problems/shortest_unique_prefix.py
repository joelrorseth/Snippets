#
# Shortest Unique Prefix
#
# Given a list of words, determine for each word, the shortest unique
# prefix to represent it distinctly. Eg. [zebra, dog, duck, dove] ->
# [z, dog, du, dov]
#
# This is easily handled using a Trie. Insert all words, but maintain a
# counter for each node, which is the # of times that node has been
# traversed over all insertions so far. This is important, to tell if
# multiple words occur past that node eg. ["bob", "bonny"]. Checking
# len(chars) wont catch these.
#
# Joel Rorseth
#

from collections import defaultdict

class Node:
    def __init__(self):
        self.chars = defaultdict(Node)
        self.isEnd = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()

    # Insert increments count of # times each node has been traversed
    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.chars:
                cur.chars[c] = Node()
            cur.count += 1
            cur = cur.chars[c]
        cur.isEnd = True

    # Make a single DFS traversal from root, stop when count = 1
    def dfs(self, word):
        cur = self.root
        path = ""
        for c in word:
            if cur.count == 1 and path != "":
                return path
            path += c
            cur = cur.chars[c]
        return word

# Find shortest prefix for each word in words
def shortest(words):

    trie = Trie()
    for w in words:
        trie.insert(w)
    return [trie.dfs(w) for w in words]



# Driver
words = ["zebra", "dog", "duck", "dove"]
print(words)
print(shortest(words))
