#
# LRU Cache
#   - Supports key, value storage and lookup (like a map)
#   - Insertion and lookup operations count as a use
#   - Least recently used item is evicted when capacity exceeded
#   - Insertion, lookup and deletion should be O(1)
#
# Joel Rorseth
#

from collections import deque

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, new_node):
        new_node.prev = None

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def pop_back(self):
        if self.tail:
            removed = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return removed

    def print_all(self):
        cur = self.head
        while cur:
            print("(%s,%s)" % (cur.key, cur.val), end="->")
            cur = cur.next
        print("None")



class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.linkedlist = DLList()
        self.cache = {}

    def get(self, key):

        # Retrieve cached node
        cached_node = self.cache[key]
        if cached_node:

            # Move node to front (if not there already)
            if cached_node.prev:
                cached_node.prev.next = cached_node.next

                if cached_node.next:
                    cached_node.next.prev = cached_node.prev

                cached_node.prev = None
                self.linkedlist.insert_front(cached_node)

            # Return node
            return cached_node.val

        return None


    def put(self, key, value):

        # Evict the least recently used if capacity is exceeded
        if len(self.cache) >= self.capacity:
            removed_node = self.linkedlist.pop_back()
            del self.cache[removed_node.key]

        # Insert new Node at front
        new_node = Node(key, value)
        self.linkedlist.insert_front(new_node)

        # Cache new Node object
        self.cache[key] = new_node


    def print_order(self):
        self.linkedlist.print_all()









# Driver
cache = LRUCache(4)
print("Put 1 then 2 then 3 then 4")
cache.put(1,1)
cache.put(2,2)
cache.put(3,3)
cache.put(4,4)
cache.print_order()
print("Put 5 then 6")
cache.put(5,5)
cache.put(6,6)
cache.print_order()
print("Get LRUCache[3] =", cache.get(3))
cache.print_order()
print("Get LRUCache[6] =", cache.get(6))
cache.print_order()
print("Get LRUCache[6] =", cache.get(6))
cache.print_order()
