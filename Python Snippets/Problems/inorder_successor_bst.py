#
# Inorder Successor
#
# Determine the successor of a given node in a binary search tree,
# relative to it's inorder traversal sequence.
#
# This solution assumes that nodes maintain a parent pointer. Worst
# case time complexity is O(h). The case of no parent pointer would
# be very similar, but if right child is null, search tree from root
# using given node's val.
#
# Joel Rorseth
#

class Node:
    def __init__(self,val,parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.val = val

class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root:
            self._insert(self.root,None,val)
        else:
            self.root = Node(val,None)

    def _insert(self,node,parent,val):
        if val < node.val:
            if node.left:
                self._insert(node.left,node,val)
            else:
                node.left = Node(val,node)
        else:
            if node.right:
                self._insert(node.right,node,val)
            else:
                node.right = Node(val,node)


    # Inorder successor
    def inorder_succ(self,node):

        # Successor is leftmost child in right, if right child exists
        if node.right:

            cur = node.right
            while cur.left:
                cur = cur.left
            return cur

        # Else, successor is parent of closest ancestor whom is a left child
        else:

            cur_parent = node.parent
            cur = node
            while cur.parent and cur.parent.left != cur:
                cur = cur_parent
                cur_parent = cur_parent.parent

            return cur_parent



# Driver
bst = BST()
bst.insert(20)
bst.insert(8)
bst.insert(4)
bst.insert(12)
bst.insert(10)
bst.insert(14)
bst.insert(22)

print(bst.inorder_succ(bst.root.left).val) # 8 -> 10
print(bst.inorder_succ(bst.root.left.right.left).val) # 10 -> 12
print(bst.inorder_succ(bst.root.left.right.right).val) # 14 -> 20
