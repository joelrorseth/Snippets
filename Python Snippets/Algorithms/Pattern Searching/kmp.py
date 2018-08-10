#
# KMP String Matching (Knuth-Morris-Pratt)
# O(m + n)
#
# Given a string 'text', determine the starting index of every occurrence
# of a string 'pattern' within 'text'. KMP is a pattern searching algorithm
# that improves upon the linear string pattern search, by avoiding repeated
# character comparisons in the subsequent checks following a match.
#
# Joel Rorseth
#


# LPS[i] is the longest proper prefix of pat[0..i] that is
# also a suffix of pat[0..i]
def build_lps(pattern):

    lps = [0]
    for c in pattern[1:]:
        j = lps[-1]

        # Find most recent lps where char was same as current char
        while j > 0 and c != pattern[j]:
            j = lps[j-1]
        if c == pattern[j]:
            j += 1
        lps.append(j)

    return lps


# Use the LPS to avoid rechecking letters in the pattern search
def find(pattern, text, lps):
    j = 0
    found_at = []

    for i in range(len(text)):

        # Use LPS to determine how many chars we need to match
        while j > 0  and text[i] != pattern[j]:
            j = lps[j-1]

        # Match this char, or confirm pattern match
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                found_at.append(i-(j-1))
                j = lps[j-1]

    return found_at




# Driver
text = "AAACABAACA"
pattern = "ACA"
print("Text: ", text)
print("Pattern: ", pattern)
print("Found at indices: ", find(pattern, text, build_lps(pattern)))
