#
# Disjoint-Set (Union-Find) data structure
#
# The union-find tracks a set of elements, partitioned into a number of
# disjoint (non-overlapping) subsets. It essentially groups elements into
# subsets by maintaining array of parents for each element. Parents have
# parents, which have parents and so on. Eventually one element is the root,
# the parent of itself, and represents the disjoint subset of all its children.
#
# Without optimizations...
# Worst case time for Union() and Find(): O(n)
#
# Joel Rorseth
#


class DisjointSet:
    def __init__(self, num_elements):
        self.parent_of = list(range(num_elements))
        self.num_subsets = num_elements

    def find(self, k):
        return k if self.parent_of[k] == k else self.find(self.parent_of[k])

    def union(self, a, b):
        parent_of_a = self.find(a)
        parent_of_b = self.find(b)

        if parent_of_a != parent_of_b:
            self.num_subsets -= 1
            self.parent_of[parent_of_a] = parent_of_b

    def print_groups(self):
        print("The DisjointSet contains %d subsets" % self.num_subsets)
        for k in range(len(self.parent_of)):
            print(k, "=> Group", self.find(k))



# This implementation, for simplicity, assumes that for n elements, the items
# contained in the disjoint set are the integers [0,n-1]. For generic use,
# map input objects to index within their original list, use with indices.

# Driver
elements = [0,1,2,3,4,5]
ds = DisjointSet(6)
ds.union(0,1)
ds.union(1,3)
ds.union(4,5)
ds.print_groups()
