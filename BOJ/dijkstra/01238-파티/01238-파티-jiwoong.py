# git commit -m "code: Solve boj 01238 파티 (jiwoong)"
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

N, M, X = map(int, input().split())

arr = [[] for _ in range(N + 1)]

dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M):
    s, e, t = map(int, input().split())
    arr[s].append((e, t))


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s][s] = 0

    while q:
        tmp = heapq.heappop(q)
        t, n = tmp[0], tmp[1]
        if dist[s][n] < t:
            continue

        for i in arr[n]:
            e, t = i[0], i[1]
            data = dist[s][n] + t
            if dist[s][e] > data:
                dist[s][e] = data
                heapq.heappush(q, (t, e))


for i in range(1, N + 1):
    dijkstra(i)

ans = -1
for i in range(1, N + 1):
    tmp = dist[i][X] + dist[X][i]
    if ans < tmp:
        ans = tmp

print(ans)
