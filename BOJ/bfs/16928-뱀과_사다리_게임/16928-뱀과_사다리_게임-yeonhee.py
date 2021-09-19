import sys
from collections import deque

input = sys.stdin.readline


def bfs(s):
    q = deque([s])
    visited[s] = 1

    while q:
        s = q.popleft()
        for i in range(1, 7):
            ns = s + i
            if ns > 100:
                break
            e = graph[ns]
            if not visited[e]:
                q.append(e)
                visited[e] = visited[s] + 1

    return visited[100]


N, M = map(int, input().split())
graph = [*range(101)]
for _ in range(N+M):
    u, v = map(int, input().split())
    graph[u] = v

visited = [0] * 101
print(bfs(1)-1)
