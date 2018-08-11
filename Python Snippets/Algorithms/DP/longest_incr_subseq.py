#
# Longest Increasing Subsequence
#
# Determine the longest subsequence (non-contiguous elements) of a
# given array A, such that the subsequence is strictly increasing.
#
# Classic DP problem. Brute force recursion solution is to include /
# exclude each eligible number, recursing to find maximal path in
# remainder. This solution makes a dp array, where dp[i] is the LIS
# possible using A[0..i].
#
# Time complexity: O(n^2)
# Space complexity: O(n)
#
# Joel Rorseth
#


def lis_length(seq):
    if not seq:
        return 0

    dp = [0] * len(seq)
    dp[0] = 1
    longest = 1

    for i in range(1, len(seq)):

        longest_ending_here = 0
        for j in range(i):
            # If seq[i] can extend increasing subseq ending at j...
            # Seek the longest of all extendable subsequences
            if seq[j] < seq[i]:
                longest_ending_here = max(longest_ending_here, dp[j])

        # Record longest ending at i, which is now 1 element longer
        dp[i] = longest_ending_here + 1
        longest = max(longest, dp[i])

    return longest



# Driver
seq = [10,9,2,5,3,7,101,18]
print(seq)
print("LIS length: ", lis_length(seq))
