from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertGraph(self, v1, v2):
        self.graph[v1].append(v2)

    def BFS(self, startNode):
        visited = set()
        queue = [] # queue
        queue.append(startNode)
        visited.add(startNode)

        while len(queue):
            cur = queue.pop(0) # FIFO
            print(cur, end=" ")

            for vertex in self.graph[cur]:
                if vertex not in visited:
                    queue.append(vertex)
                    visited.add(vertex)

g = Graph()

# 2 -> (1,5)   5 -> (6,8)   6 -> (9)

g.insertGraph(2,1)
g.insertGraph(2,5)
g.insertGraph(5,6)
g.insertGraph(5,8)
g.insertGraph(6,9)

g.BFS(2)
