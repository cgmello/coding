import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, N, K):
        g = defaultdict(list)

        for u, v, cost in times:
            g[u].append((cost, v))  # tuple (distance, node)

        print(g)

        min_heap = [(0, K)]

        visited = set()

        # {1: inf, 2: inf, 3: inf, 4: inf}
        distance = {i: float('inf') for i in range(1, N + 1)}
        distance[K] = 0

        print(distance)

        while min_heap:
            cur_distance, u = heapq.heappop(min_heap) # pop smallest distance
            if u in visited:
                continue
            visited.add(u)

            if len(visited) == N:
                return cur_distance

            for direct_distance, v in g[u]:
                if cur_distance + direct_distance < distance[v] and \
                        v not in visited:
                    distance[v] = cur_distance + direct_distance
                    heapq.heappush(min_heap, (distance[v], v))

        return -1


times = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]
N = 4
K = 2

s = Solution()
print(s.networkDelayTime(times, N, K))
