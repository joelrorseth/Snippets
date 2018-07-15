#
# Weighted Directed Acyclical Graph (DAG)
# Joel Rorseth
#

from collections import defaultdict, deque
from heapq import heappush, heappop


class Graph:
    def __init__(self):
        self.adj = defaultdict(set)
        self.vert = set()

    def connect(self, v1, v2, weight):
        self.adj[v1].add((v2, weight))
        self.vert.add(v1)
        self.vert.add(v2)

    def print(self):
        for v, adj_list in self.adj.items():
            print(v, ":", adj_list)

    # Simple non-recursive DFS - O(V+E)
    def dfs(self, start):
        vis = set()
        stack = [start]

        while stack:
            cur = stack.pop()

            if cur not in vis:
                vis.add(cur)

                print(cur)
                stack += [ v for v,w in self.adj[cur] ]

    # Simple non-recursive BFS - O(V+E)
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

    # Determine ordering such that for every edge u-v, vertex u comes first.
    # O(V+E)  Modified DFS yields same complexity.

    def topo(self):
        order = []
        vis = set()

        for v in self.vert:
            self._topo(v, order, vis)
        return order

    def _topo(self, v, order, vis):
        if v not in vis:
            vis.add(v)
            for adj_v, _ in self.adj[v]:
                self._topo(adj_v, order, vis)

            order.append(v)

    # Determine shortest distances/paths from start node to all nodes
    # O(E+V)*(logV)  aka O(ElogV). Using minheap for shortest dist is log

    def dijkstra(self, start):
        vis = set()
        distances = [(0, start)]

        while distances:
            cur_dist, cur = heappop(distances)
            if cur not in vis:
                vis.add(cur)
                print("%d -> %d: %d" % (start, cur, cur_dist))

                for adj, adj_weight in self.adj[cur]:
                    heappush(distances, (cur_dist+adj_weight, adj))



g = Graph()
g.connect(1,2,3)
g.connect(2,3,4)
g.connect(2,6,2)
g.connect(3,5,6)
g.connect(5,7,5)
g.connect(6,5,9)
g.connect(3,7,4)
g.print()
print("\nTopological Sort: ", g.topo())
print("\nDijkstra for src=1:")
g.dijkstra(1)
