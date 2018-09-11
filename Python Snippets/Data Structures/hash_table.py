#
# Simple Hash Table implementation
#  - Provide key-value lookup
#  - Should handle collisions (chaining)
#  - Should support dynamic resizing
#
# Joel Rorseth
#

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lookup = [[] for _ in range(capacity)]

    # Simple hash function will convert to int and % capacity
    def calculate_hash(self, key):
        return hash(key) % self.capacity

    # Insertion will simply append to list at hash idx (chaining)
    def put(self, key, value):
        hashed_index = self.calculate_hash(key)
        self.lookup[hashed_index].append(HashNode(key, value))

    # Retrieval will linear search the list at the hash idx, look for key match
    def get(self, key):
        hashed_index = self.calculate_hash(key)

        for node in self.lookup[hashed_index]:
            if node.key == key:
                return node.value
        return None

    def debug(self):
        for idx in range(len(self.lookup)):
            print(idx, [node.value for node in self.lookup[idx]])




# Driver
t = HashTable(3)
t.put(1,1)
t.put(2,2)
t.put(3,3)
t.put(4,4)
t.get(1)
t.get(4)
t.debug()
