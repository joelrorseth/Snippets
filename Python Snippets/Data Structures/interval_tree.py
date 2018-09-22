#
# Augmented Interval Tree
#
# An augmented binary search tree used to store intervals. Supported
# operations should include insertion, deletion, and the ability to query
# for stored intervals that overlap with a query interval.
#
# Note: When implemented as a self-balancing BST (AVL, Red-Black etc),
# the supported operations should run in O(log n).
#
# Joel Rorseth
#

class Node:
    def __init__(self, interval):
        self.start = interval[0]
        self.end = interval[1]
        self.max_val = interval[1]
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.start < other.start:
            return True
        elif self.start == other.start and self.end <= other.end:
            return True
        else:
            return False


class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, interval):
        if not self.root:
            self.root = Node(interval)
        else:
            self._insert(self.root, Node(interval))


    # Insert left or right, based on well defined ordering (start)
    # Update max (end) val in subtree rooted at current root
    def _insert(self, root, new_node):

        if new_node.max_val > root.max_val:
            root.max_val = new_node.max_val

        if new_node < root:
            if root.left:
                self._insert(root.left, new_node)
            else:
                root.left = new_node
        else:
            if root.right:
                self._insert(root.right, new_node)
            else:
                root.right = new_node

    # TODO: Overlap query

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print("(%d,%d), max=%d" % (root.start, root.end, root.max_val))
            self._inorder(root.right)





# Driver
tree = IntervalTree()
tree.insert((5,10))
tree.insert((15,25))
tree.insert((1,12))
tree.insert((8,16))
tree.insert((14,20))
tree.insert((18,21))
tree.insert((2,8))
tree.inorder()
