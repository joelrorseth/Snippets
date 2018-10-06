#
# Given a pattern containing the characters I and D, where I denotes
# increasing and D denotes decreasing. Devise an alogrithm to print the
# minimum number that conforms to this pattern. Digits must be unique,
# therefore only use 1-9 once.
#
# Ex:  D -> 21
#      II -> 123
#
# Joel Rorseth
#

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder(self):
        if self.left:
            yield from self.left.inorder()
        yield self.val
        if self.right:
            yield from self.right.inorder()


#
# Solution: Use BST to build decreasing sequences (left branches)
# that can be formed (in reverse) using an inorder traversal.
#
#                1             Ex. DDIDDIID
#             /     \           -> 321654798 via inorder trav.
#           2         4
#         /         /   \
#       3          5      7
#                /         \
#               6            8
#                           /
#                         9

def decode(pattern):

    root = Node(1)
    counter = 2
    _i = root
    _d = root

    for c in pattern:
        if counter > 9:
            return -1 # Invalid

        new_node = Node(counter)
        counter += 1

        # I will end current decreasing left branch, move right
        if c == "I":
            _i.right = new_node
            _i = new_node
            _d = new_node
        # D will add counter to left, continuing the decreasing branch
        elif c == "D":
            _d.left = new_node
            _d = new_node

    return "".join([str(i) for i in root.inorder()])






# Driver
pat = "DDIDDIID"
print("Given", pat, ", min number is", decode(pat))
