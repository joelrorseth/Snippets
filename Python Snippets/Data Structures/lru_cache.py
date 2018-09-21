#
# LRU Cache
#   - Supports key, value storage and lookup (like a map)
#   - Insertion and lookup operations count as a use
#   - Least recently used item is evicted when capacity exceeded
#   - Insertion, lookup and deletion should be O(1)
#
# Note 1: Should use doubly linked list, we use deque here
#
# Joel Rorseth
#

from collections import deque

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()
        self.lookup = {}

    def insert(self, key, value):

        if len(self.queue) == self.capacity:
            self.queue.pop()

        self.queue.appendleft((key, value))
        self.lookup[key] =
