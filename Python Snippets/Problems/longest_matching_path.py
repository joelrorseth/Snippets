"""
In this problem we consider an undirected tree with N nodes, numbered
from 1 to N. Additionally, each node also has a label attached to it
and the label is an integer value. Note that different nodes can have
identical labels.

Write a function:

 solution(A, E)

that, given a zero-indexed array A of length N, where A[J] is the label
value of the (J+1)-thnode in the tree, and a zero-indexed array E of
length K = (N-1) * 2 in which the edges of the tree are described
(for every 0 ≤ J < N - 2 values E[2 * J] and E[2 * J + 1] represents an
edge connecting node E[2 * J] with node E[2 * J + 1]), returns the length
of the longest path such that all the nodes on that path have the same
label. The length of a path is defined as the number of edges in that path.

For example, given A = [1, 1, 1, 2 , 2] and E = [1, 2, 1, 3, 2, 4, 2, 5],
the described tree appears as follows:

     1(1)
    /    \
  2(1)    3(1)
  /    \
4(2)   5(2)

and your function should return 2, because the longest path (in which
all nodes have the same value of 1) is 2 → 1 → 3. The number of edges
on this path is 2; thus, that is the answer.

Assume that:
* 1 ≤ N ≤ 1,000
* each element of array A is an integer within the range [1..1,000,000,000].
"""

from collections import defaultdict

# Given tree (acyclic), find longest matching path for each (non-leaf) node
def solution(A, E):

    adj = defaultdict(list)
    for j in range(len(A)-1):

        n1, n2 = E[2*j], E[2*j+1]
        adj[n1].append(n2)

    nonleafs = list(adj.keys())
    return max(longest_match_from(n, adj, A) for n in nonleafs)


# Given a node, find the longest path of consecutive label matches starting here
# Check all adj nodes (with same label) for their longest path
def longest_match_from(cur, adj, labels):

    matches = list(filter(lambda n: labels[n-1] == labels[cur-1], adj[cur]))
    if not matches:
        return 1

    return 1 + sum(longest_match_from(m, adj, labels) for m in matches)



# Driver
a = [1,1,1,2,2]
e = [1,2,1,3,2,4,2,5]
print("Labels: ", a)
print("Edges: ", e)
print("Longest path of same label: ", solution(a,e))
