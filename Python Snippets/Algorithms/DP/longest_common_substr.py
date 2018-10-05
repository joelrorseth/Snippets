#
# Longest Common Substring (DP)
# O(m*n) time and space
#
# Classic DP problem: You are essentially finding the longest common suffix
# between all prefixes. DP table builds from "" vs "", then finds LCS("A","")
# and so on. For dp[i][j], you are finding LCS(a[ending at i], b[ending at j]).
# If a[i] and b[j] are char match, chop those chars off and add 1 to
# LCS(a[ending at i-1, b[ending at j-1]).
#
# Joel Rorseth
#

def lcs(a, b):

    dp = [[0 for c in range(len(b)+1)] for r in range(len(a)+1)]
    maxlen = 0
    maxend = len(a)

    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):

            # If matched at these pointers, LCS is 1 + LCS(a[0..i-2],b[0..j-2])
            # This corresponds to diagonally up->left value in dp, dp[i-1][j-1]
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

                if dp[i][j] > maxlen:
                    maxlen = dp[i][j]
                    maxend = i

    return a[(maxend - maxlen):maxend]



# Driver
a = "ABCBA"
b = "BABCA"
print("A: %s, B: %s" % (a,b))
print("Longest common substring: %s" % lcs(a,b))
