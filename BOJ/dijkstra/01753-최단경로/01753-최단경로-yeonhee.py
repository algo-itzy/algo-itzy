import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    dp[start] = 0

    while q:
        w, now = heappop(q)
        for _n, _w in graph[now]:
            nw = _w + w
            if nw < dp[_n]:
                dp[_n] = nw
                heappush(q, [nw, _n])


v, e = map(int, input().split())
k = int(input())

graph = defaultdict(list)
dp = [float('inf')] * (v+1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)

print(*[i if i != float('inf') else "INF" for i in dp[1:]], sep='\n')
