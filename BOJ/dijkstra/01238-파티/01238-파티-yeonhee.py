import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def dijkstra(s):
    distance = [float('inf')] * (n + 1)
    heap = []
    heappush(heap, [0, s])
    distance[s] = 0

    while heap:

        now_cost, node = heappop(heap)
        for next_cost, next_node in graph[node]:
            next_cost = next_cost + now_cost

            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heappush(heap, [next_cost, next_node])

    return distance


n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([t, b])

result = 0

for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)
