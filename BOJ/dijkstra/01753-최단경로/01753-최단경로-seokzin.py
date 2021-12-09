import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(x):
    dp[x] = 0
    heapq.heappush(heap, [0, x])

    while heap:
        now_w, now = heapq.heappop(heap)

        for new, new_w in graph[now]:
            cal_w = now_w + new_w
            
            if cal_w < dp[new]:
                dp[new] = cal_w
                heapq.heappush(heap, [cal_w, new])


v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)] 
dp = [INF] * (v+1)
heap = []

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dijkstra(k)

for i in dp[1:]:
    print(i if i != INF else "INF")