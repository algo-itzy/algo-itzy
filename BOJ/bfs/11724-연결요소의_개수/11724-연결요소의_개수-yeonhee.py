import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v):
    visited[v] = 1
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
