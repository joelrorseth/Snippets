#
# Suffix Array
#
# Suffix array is simply an alphabetically sorted array of all possible
# suffixes of a single, given string. It is useful for pattern searching
# and for problems such as Longest Repeated Substring. Worth noting
# that it is a alternate data structure in place of a suffix tree.
#
# Joel Rorseth
#

# Suffix only stores start index, not actual sliced text
class Suffix:

    def __init__(self, s, i):
        self.string = s
        self.index = i

    def __lt__(self, other):
        return self.string[self.index:] < other.string[other.index:]

    def to_string(self):
        return self.string[self.index:]


# Suffix Array construction is O(n lgn)
class SuffixArray:

    def __init__(self, text):
        self.suffixes = [Suffix(text, i) for i in range(len(text))]
        self.suffixes.sort()

    def list(self):
        for s in self.suffixes:
            print(s.to_string())



# Driver
sa = SuffixArray("hello")
sa.list()
