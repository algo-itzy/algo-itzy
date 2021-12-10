import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    hq = []
    dis = [INF] * (n+1)

    heapq.heappush(hq, (0, start))
    dis[start] = 0

    while hq:
        d, x = heapq.heappop(hq)

        if dis[x] < d:
            continue

        for nx, nw in graph[x]:
            w = d + nw

            if dis[nx] > w:
                dis[nx] = w
                heapq.heappush(hq, (w, nx))

    return dis


n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
res = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

back = dijkstra(x)

for i in range(1, n+1):
    go = dijkstra(i)
    res = max(res, go[x]+back[i])

print(res)