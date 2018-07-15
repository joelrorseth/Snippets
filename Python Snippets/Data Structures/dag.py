#
# Weighted Directed Acyclical Graph (DAG)
# Joel Rorseth
#

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.adj = defaultdict(set)
        self.vert = set()

    def connect(self, v1, v2, weight):
        self.adj[v1].add((v2, weight))
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

    def bfs(self, start):
        vis = set()
        q = deque([start])

        while q:
            cur = q.popleft()

            if cur not in vis:
                vis.add(cur)

                print(cur)
                for v,w in self.adj[cur]:
                    q.append(v)


g = Graph()
g.connect(1,2,3)
g.connect(2,3,4)
g.connect(2,6,2)
g.connect(3,5,6)
g.connect(5,7,5)
g.bfs(1)
