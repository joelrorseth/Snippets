#
# Combinations
#
# Given two integers n and size, generate all possible unqique combinations of
# size numbers, using the numbers 1..n.
#
# Classic Backtracking problem. Must recusrively generate all possible combos.
# Essentially, each number i can be selected or not, then recurse for [i+1,n].
# At each recursion, attempt to insert next all valid numbers coming after
# j, the previous value selected by recursive caller.
#
# Joel Rorseth
#

def backtrack(v, row, i, n, size):
    # Combo size has been reached
    if size == 0:
        v.append(row)
        return

    # No numbers can be added to this combination since pointer i == n
    if i == n:
        return

    # j from [i,n) can be combined with (size-1) numbers after it, from (j,n)
    for j in range(i, n):
        backtrack(v, row+[j+1], j+1, n, size-1)


def combine(n, size):
    v = []
    backtrack(v, [], 0, n, size)
    return v



# Driver
n = 4
size = 2
print("Using 1..%d, All combinations of size %d:" % (n, size))
print(combine(n, size))
