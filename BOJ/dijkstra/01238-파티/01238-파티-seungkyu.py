# git commit -m "code: Solve boj 01238 파티 (seungkyu)"
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    dists = [float('inf')]*(N+1)
    q = []
    heapq.heappush(q, (0, start))
    dists[start] = 0

    while q:
        cur_dist, cur = heapq.heappop(q)

        if dists[cur] < cur_dist:
            continue

        for new_pos, new_cost in graph[cur]:
            dist = cur_dist + new_cost

            if dist < dists[new_pos]:
                dists[new_pos] = dist
                heapq.heappush(q, (dist, new_pos))

    return dists


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

ans = 0
for i in range(1, N+1):
    ans = max(ans, dijkstra(i)[X] + dijkstra(X)[i])

print(ans)