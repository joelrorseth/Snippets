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

    def remove(self,val):
        slow = None
        fast = self.head

        while fast:
            if fast.val == val:
                if slow:
                    slow.next = fast.next
                else:
                    self.head = self.head.next
                return True

            slow = fast
            fast = fast.next

        return False

    def print(self):
        n = self.head
        while n:
            print(n.val, end=" -> ")
            n = n.next
        print("None")


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.print()
ll.remove(3)
ll.print()
ll.remove(5)
ll.print()
