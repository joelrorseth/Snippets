#
# Singly Linked List
# Joel Rorseth
#

class Node:
    def __init__(self,val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,val):
        n = Node(val)
        n.next = self.head
        self.head = n

    def print(self):
        n = self.head
        while n:
            print(n.val)
            n = n.next



ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.print()
