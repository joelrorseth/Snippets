#
# Doubly Linked List
#
# This implementation maintains a next and previous pointer for each node,
# and each list maintains a head and tail. This yeilds improvements over
# singly linked lists, including the ability to insert / remove from either
# end in O(1), as well as easy fwd / bkwd traversal in O(n).
#
# Joel Rorseth
#

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, val):
        new_node = Node(val)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_back(self, val):
        new_node = Node(val)

        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head:
            self.head.next.prev = None
            self.head = self.head.next

    def pop_back(self):
        if self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def print(self):
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")





ll = DLList()
ll.insert_front(3)
ll.insert_front(2)
ll.insert_front(1)
ll.insert_back(4)
ll.insert_back(5)
ll.print()
ll.pop_front()
ll.print()
ll.pop_back()
ll.print()
