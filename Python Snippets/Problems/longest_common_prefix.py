#
# Find longest common prefix (LCP) of a set of words
# Ex. {coder, code, corner} => "co"
#

# Q: Will there always be words in set? More than 1?

from collections import defaultdict


class Node:
    def __init__(self):
        self.isEnd = False
        self.chars = defaultdict(Node)


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self,string):
        cur = self.head

        for c in string:
            if not c in cur.chars:
                cur.chars[c] = Node()

            cur = cur.chars[c]

        cur.isEnd = True


    # Insert all words into the trie, traverse
    # Common prefix must have only 1 child node at each letter
    def lcp(self,words):
        if not words:
            return ""

        guide = next(iter(words)) # Grab any word
        for w in words:
            self.insert(w)

        cur = self.head
        length = 0

        while len(cur.chars) == 1 and not cur.isEnd:
            cur = cur.chars[guide[length]]
            length += 1

        return guide[:length]



s1 = {"code","coder","coral"}
print(s1)
print("LCP: %s" % t.lcp(s1))
