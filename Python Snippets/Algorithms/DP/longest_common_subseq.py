#
# Longest Common Subsequence
#
# Given two sequences A and B, find length of longest subsequence present in
# both. A subsequence is defined as a sequence whose elements appear in order
# in another sequence, though not necessarily contiguous to eachother.
#
# Classic DP Problem: Build up to LCS length, starting w/ LCS length of "" and
# "". As you iterate each combo a[i] and b[j], if chars match, LCS length is 1
# plus the LCS( a[0..i-1], b[0..j-1] ). Otherwise, it's simply equal to the
# longest LCS of a (or b) minus one letter.
#
# Joel Rorseth
#


# Time & Space Complexity: O(mn)
def lcs(a, b):

    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

    for i in range(1,len(a)+1):
        for j in range(1, len(b)+1):

            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]



# Time complexity: O(mn), Space: O(n)
def lcs_optimized(a, b):

    dp = [[0 for _ in range(len(b)+1)] for _ in range(2)]
    dp_row = bool

    for i in range(len(a)):
        dp_row = i&1

        for j in range(len(b)+1):

            if i==0 or j==0:
                dp[dp_row][j] = 0
            elif a[i] == b[j-1]:
                dp[dp_row][j] = 1 + dp[1-dp_row][j-1]
            else:
                dp[dp_row][j] = max(dp[1-dp_row][j], dp[dp_row][j-1])

    return dp[dp_row][-1]





# Driver
a = "AGGTAB"
b = "GXTXAYB"
print("Given", a, ",", b)
print("Longest common subsequence length:", lcs(a,b))
