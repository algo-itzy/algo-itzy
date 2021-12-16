# git commit -m "code: Solve boj 01238 파티 (seungjoo)"
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start, dist, graph):
    heap = []
    dist[start] = 0
    heappush(heap, [0, start])
    while heap:
        cur_cost, cur_node = heappop(heap)
        if dist[cur_node] < cur_cost:
            continue
        for next_node, next_cost in graph[cur_node]:
            costs = next_cost + cur_cost
            if costs < dist[next_node]:
                dist[next_node] = costs
                heappush(heap, [costs, next_node])

n, m, x = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
reverse_graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    reverse_graph[b].append([a, t])

dist = [float('inf')] * (n + 1)
reverse_dist = [float('inf')] * (n + 1)
dijkstra(x, dist, graph)
dijkstra(x, reverse_dist, reverse_graph)

max_dist = 0
for i in range(1, n + 1):
    max_dist = max(max_dist, dist[i] + reverse_dist[i])
print(max_dist)