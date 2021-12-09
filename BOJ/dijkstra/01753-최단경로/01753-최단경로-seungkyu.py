# git commit -m "code: Solve boj 01753 최단경로 (seungkyu)"
import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, cur = heapq.heappop(q)

        if dists[cur] < dist:
            continue

        for node in graph[cur]:
            cost = dist + node[1]
            if cost < dists[node[0]]:
                dists[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
dists = [float('inf')]*(V+1)
dists[K] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V+1):
    if dists[i] == float('inf'):
        print('INF')
    else:
        print(dists[i])