#
# Trie (Prefix Tree)
# Joel Rorseth
#

from collections import defaultdict


class Node:
    def __init__(self):
        self.isEnd = False
        self.chars = defaultdict(Node)


class Trie:
    def __init__(self):
        self.head = Node()

    # Insert a string
    def insert(self,string):
        cur = self.head

        for c in string:
            if not c in cur.chars:
                cur.chars[c] = Node()

            cur = cur.chars[c]

        cur.isEnd = True

    # Simple DFS, check for leaf to print current string
    def print_all(self):
        self._print_all(self.head,"")

    def _print_all(self, cur, s):

        if cur.isEnd:
            print(s)

        # Recurse, pass on new current word w/ letter added
        for c, node in cur.chars.items():
            self._print_all(node, s+c)



t = Trie()
t.insert("code")
t.insert("coder")
t.insert("comic")
t.insert("croak")
t.insert("dog")
t.print_all()
