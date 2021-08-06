import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx >= m or nx < 0 or ny >= n or ny < 0:
            continue

        if graph[ny][nx] == 1:
            graph[ny][nx] = 0  # 방문 지점은 0으로 만든다.
            dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    cnt = 0
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1  # 해당 지역의 DFS가 끝났을 때 cnt를 증가시킨다.

    print(cnt)

# DFS 기본적인 문제
# 재귀 리밋을 늘려줘야했다.