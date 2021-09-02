from collections import deque


def dfs(x):
    visited[x] = 1
    print(x, end=' ')
    for i in range(1, N + 1):
        if visited[i] == 0 and graph[x][i] == 1:
            dfs(i)


def bfs(x):
    queue = deque([x])
    visited[x] = 0
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N + 1):
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 0


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    num1, num2 = map(int, input().split())
    graph[num1][num2] = graph[num2][num1] = 1

visited = [0] * (N + 1)
dfs(V)
print()
bfs(V)
