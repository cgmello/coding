def isSafe(graph, color):
    # check for every edge
    for i in range(4):
        for j in range(i + 1, 4):
            if (graph[i][j] and color[j] == color[i]):
                return False
    return True

def graphColoring(graph, m, i, color):
    # if current index reached end
    if (i == 4):
        # if coloring is safe
        if (isSafe(graph, color)):
            for i in range(4):
                print(color[i],end=" ")
            return True
        return False

    # Assign each color from 1 to m
    for j in range(1, m + 1):
        color[i] = j

        # Recur of the rest vertices
        if (graphColoring(graph, m, i + 1, color)):
            return True
        color[i] = 0
    return False

graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
]
m = 3  # Number of colors
color = [0 for i in range(4)]
result = graphColoring(graph, m, 0, color)
print(result)
