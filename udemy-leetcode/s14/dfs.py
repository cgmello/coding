from collections import defaultdict


# Depth First Search
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertGraph(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, startNode):
        visited = set()
        st = [] # stack
        st.append(startNode)

        while len(st):
            cur = st[-1] # LIFO
            st.pop()

            if cur not in visited:
                print(cur, end=" ")
                visited.add(cur)

            for vertex in self.graph[cur]:
                if vertex not in visited:
                    st.append(vertex)

g = Graph()

# 2 -> (1,5)   5 -> (6,8)   6 -> (9)

g.insertGraph(2,1)
g.insertGraph(2,5)
g.insertGraph(5,6)
g.insertGraph(5,8)
g.insertGraph(6,9)

g.DFS(2)
