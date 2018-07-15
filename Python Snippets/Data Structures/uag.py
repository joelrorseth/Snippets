#
# Weighted Undirected Acyclical Graph
# Joel Rorseth
#

from collections import defaultdict


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


g = Graph()
g.connect(1,2,3)
g.connect(2,3,4)
g.connect(2,6,2)
g.connect(4,6,6)
g.connect(5,6,5)
g.dfs(1)
