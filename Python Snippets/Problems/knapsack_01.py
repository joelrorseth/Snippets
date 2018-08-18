#
# 0-1 Knapsack Problem
#
# You are given a set of n items, in the form of two arrays (val and weight)
# of size n. Each ith item has weight = weight[i] and value = val[i]. Given
# the maximum carrying weight of a knapsack, determine max total value that
# can be stored in the knapsack, by storing or not storing each item.
#
# Naive solution O(2^n): Use recursion to either keep or discard each element,
# recursing to do the same to remainder for each of those two subcases.
#
# Classic DP solution: O(n * capacity)
# Build dp table for each fraction of capacity, with each row considering more
# and more items. Record max value for each capacity fraction, by either not
# including an item, or including by adding to best previous value that could
# occur within the leftover capacity in knapsack.
#
# Joel Rorseth
#


def knapsack(capacity, weight, val):
    n = len(val)

    # Each item gets a row, each fraction of capacity gets a column
    dp = [[0 for c in range(capacity+1)] for r in range(n+1)]

    for r in range(1, n+1):
        cur_w = weight[r-1]
        cur_v = val[r-1]
        for c in range(1, capacity+1):
            skip_over = dp[r-1][c]
            include = dp[r-1][c - cur_w] + cur_v

            # Put in knapsack or don't, depending on which maximizes val
            if cur_w <= c:
                dp[r][c] = max(skip_over, include)
            else:
                dp[r][c] = skip_over

    return dp[-1][-1]




# Driver
values = [100,20,60,40]
weights = [3,2,4,1]
capacity = 5
print("Values: ", values, "\nWeights: ", weights, "\nCapacity: ", capacity)
print("Maximized value: ", knapsack(capacity, weights, values))
