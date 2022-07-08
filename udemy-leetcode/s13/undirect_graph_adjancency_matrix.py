class Graph:
    def __init__(self, numberOfNodes):
        # 4 => 0,1,2,3,4 (total=5)
        self.numberOfNodes = numberOfNodes + 1
        self.graph = [
            [0 for x in range(numberOfNodes + 1)]
            for y in range(numberOfNodes + 1)
        ]

    def withInBounds(self, v1, v2):
        return v1 >= 0 and v1 <= self.numberOfNodes and v2 >= 0 and \
            v2 <= self.numberOfNodes

    def insertEdge(self, v1, v2):
        if self.withInBounds(v1, v2):
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1 # ONLY THIS LINE

    def printGraph(self):
        for i in range(self.numberOfNodes):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print(f"{i} -> {j}")


g = Graph(5)

# 1 -> 2 -> 3    4 -> 5
g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()