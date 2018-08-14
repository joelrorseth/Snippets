#
# Weighted Undirected Acyclical Graph
# Joel Rorseth
#

from collections import defaultdict
from heapq import heappush, heappop, heapify

class Graph:
    def __init__(self):
        self.adj = defaultdict(set)
        self.vert = set()

    def connect(self, v1, v2, weight):
        self.adj[v1].add((v2, weight))
        self.adj[v2].add((v1, weight))
        self.vert.add(v1)
        self.vert.add(v2)

    def dfs(self, start):
        vis = set()
        stack = [start]

        while stack:
            cur = stack.pop()

            if cur not in vis:
                vis.add(cur)

                print(cur)
                stack += [ v for v,w in self.adj[cur] ]


    # Generate Minimum Spanning Tree (Prim's algo) in O(E log V)
    # Best choice for dense graphs over Kruskal's algo

    def prim_mst(self, start):
        mst = defaultdict(set)
        vis = set([start])

        edges = [(w, start, adj) for adj, w in self.adj[start]]
        heapify(edges)

        while edges:
            # Pop min weight adj node in edges set, add "to->frm" to MST
            weight, frm, to = heappop(edges)
            if to not in vis:
                vis.add(to)
                mst[frm].add(to) # Build the tree (adj list)

                # Min's adjacents are up next, add into heap w/ cost
                for adj, adj_w in self.adj[to]:
                    if adj not in vis:
                        heappush(edges, (adj_w, to, adj))

        return mst



g = Graph()
g.connect(1,2,2)
g.connect(1,3,3)
g.connect(2,3,1)
g.connect(2,4,1)
g.connect(2,5,4)
g.connect(3,6,5)
g.connect(4,5,1)
g.connect(5,6,1)
g.connect(6,7,1)
print(g.prim_mst(1))
