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

# Suffix Array construction is O(n lgn)
class SuffixArray:

    def __init__(self, s):
        self.string = s
        self.isuffixes = sorted(range(len(s)), key=lambda i: s[i:])

    def list(self):
        for i in self.isuffixes:
            print(self.string[i:])

    # LCP of two suffixes starting at given indices
    def lcp(self, i, j):
        longest = ""
        n = len(self.string)
        while i < n and j < n and self.string[i]==self.string[j]:
            longest += self.string[i]
            i += 1
            j += 1
        return longest

