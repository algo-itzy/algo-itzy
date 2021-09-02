import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
# 정점의 개수 n, 간선의 개수 m, 탐색 시작할 정점의 번호 v

graph =[[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 0

    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in range(1, n+1):
            if visited[i] ==1 and graph[v][i] ==1:
                queue.append(i)
                visited[i] =0

def dfs(v):
    visited[v] = 1
    print(v, end =' ')
    for i in range(1, n+1):
        if visited[i] ==0 and graph[v][i]==1:
            dfs(i)

dfs(v)
print()
bfs(v)

# git commit -m "code: Solve boj 01260 DFS와 BFS (yeonju)"