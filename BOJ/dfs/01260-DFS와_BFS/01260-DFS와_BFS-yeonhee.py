import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1


N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph.keys():  # 정렬
    graph[i] = sorted(set(graph[i]))

visited = [0] * (N+1)
dfs(V)
print()

visited = [0] * (N+1)
bfs(V)
