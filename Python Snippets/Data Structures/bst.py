#
# Simple Binary Search Tree
# Joel Rorseth
#

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self,val):
        if self.root:
            self._insert(self.root,val)
        else:
            self.root = Node(val)

    def _insert(self,current,val):
        if val < current.val:
            if current.left:
                self._insert(current.left,val)
            else:
                current.left = Node(val)
        else:
            if current.right:
                self._insert(current.right,val)
            else:
                current.right = Node(val)

    # Inorder trav
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self,root):
        if root:
            self._inorder(root.left)
            print(root.val)
            self._inorder(root.right)



bst = BST()
bst.insert(7)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(2)
bst.insert(4)
bst.inorder()

