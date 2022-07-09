class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0 for column in range(n)] for row in range(n)]

    def isSafe(self, v, color, c):
        for i in range(self.n):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
            return True

    def graphColoringUtil(self, m, color, v):
        if v == self.n:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, color, c):
                color[v] = c
                if self.graphColoringUtil(m, color, v + 1):
                    return True
                color[v] = 0

    def graphColoring(self, m):
        color = [0] * self.n

        if self.graphColoringUtil(m, color, 0) == None:
            return False

        # print
        for c in color:
            print(c, end=" ")

        return True

g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
g.graphColoring(m)
