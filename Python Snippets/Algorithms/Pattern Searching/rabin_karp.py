#
# Rabin-Karp String Search Algorithm
# https://brilliant.org/wiki/rabin-karp-algorithm/
#
# Rabin-Karp is a string searching algorithm that uses hashing to find
# patterns in strings. This "Rolling Hash" efficiently recalculates hashes for
# adjacent substrings, by reusing the hash values of overlapped, already-
# calculated chars. It is otherwise almost identical to naive string search.
#
# Worst case time: O(n*m)
#  *Avg case time: O(n+m)
#
# Joel Rorseth
#


class Hash:
    def __init__(self, haystack, len_needle):
        self.haystack = haystack
        self.hash = 0
        self.len_needle = len_needle

        # Combine hashes for letters in starting needle window [0,len_needle-1]
        # Ex.  Hash("abc") = 1*26^2 + 2*26^1 + 3*26^0

        for i in range(len_needle):
            char_as_num = ord(self.haystack[i]) - ord("a") + 1
            exp_hash_term =  26 ** (len_needle - i - 1)
            self.hash += char_as_num * exp_hash_term

        self.window_start = 0
        self.window_end = len_needle

    # Move window that hash is covering (needle size) to the right by 1
    def move_window(self):
        if self.window_end <= len(self.haystack) - 1:
            old_start_as_num = ord(self.haystack[self.window_start]) - ord("a") + 1
            new_end_as_num = ord(self.haystack[self.window_end]) - ord("a") + 1

            # Subtract out leftmost (start) term, increment powers of other exp terms
            # by multiplying by 26, then add hash for new term to the right
            # Ex.  Hash("bcd") = ((1*26^2 + 2*26^1 + 3*26^0) - 1*26^2) * 26 + 4*26^0

            self.hash -= old_start_as_num * 26**(self.len_needle-1)
            self.hash *= 26
            self.hash += new_end_as_num  # This is actually (num * 26^0)
            self.window_start += 1
            self.window_end += 1

    def to_string(self):
        return self.haystack[self.window_start : self.window_end]



def rabin_karp(needle, haystack):
    if needle == "" or haystack == "" or len(needle) > len(haystack):
        return None

    rolling_hash = Hash(haystack, len(needle))
    needle_hash = Hash(needle, len(needle))

    for i in range(len(haystack) - len(needle) + 1):
        # If needle and haystack hashes match, verify then output match!
        if rolling_hash.hash == needle_hash.hash:
            if rolling_hash.to_string() == needle:
                return i

        rolling_hash.move_window()
    return None




# Driver
print("Needle: \"dog\", Haystack: \"hotdog\"")
print("Found at position ", rabin_karp("dog", "hotdog"))
