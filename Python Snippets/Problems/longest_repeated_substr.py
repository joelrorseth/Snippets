#
# Longest Repeated Substring (suffix array solution)
#
# Given a single string, determine the longest substring which appears
# within the given string at two or more locations.
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

    # The LCP between any adjacent suffixes is the longest repeated substring
    def lcp_adj(self):
        longest = ""
        for i in range(len(self.string)-1):
            prefix = self.lcp(self.isuffixes[i], self.isuffixes[i+1])

            if len(prefix) > len(longest):
                longest = prefix

        return longest



def lrs(strings, answers):
    print("Longest Repeated Substring")
    for (i, s) in enumerate(strings):
        sa = SuffixArray(s)
        longest = sa.lcp_adj()

        print("%s %s ==> %s" % (("✓" if longest==answers[i] else "✖"), s, longest))


# Driver
_input = ["ABCDXXXABCD", "ABCABC", "ABC", "ABCA", "AXXA", "ABCDEFXYXYXYABCDEF",\
        "ABRACADABRA"]
_output = ["ABCD", "ABC", "", "A", "A", "ABCDEF", "ABRA"]
lrs(_input, _output)
