from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def bfs(x):
    visited[x] = 1
    q = deque([x])

    while q:
        v = q.popleft()
        for nodes in graph[v]:
            if not visited[nodes]:
                visited[nodes] = True
                q.append(nodes)


ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        ans += 1
        bfs(i)

print(ans)
