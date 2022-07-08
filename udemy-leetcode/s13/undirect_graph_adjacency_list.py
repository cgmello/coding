from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    # (1,2): 1 => 2 : #1 => [2]
    # (1,3): 1 => 3 : #1 => [2,3]
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1) # ONLY THIS LINE
        
    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print(f"{node} -> {v}")
            

g = Graph()
            
# 1 -> 5,100 -> 2 -> 7 -> 1
g.insertEdge(1, 5) 
g.insertEdge(1, 100) 
g.insertEdge(5, 2)
g.insertEdge(2, 7)
g.insertEdge(7, 1)

g.printGraph()
