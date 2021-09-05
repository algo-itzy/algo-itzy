import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    graph[x][y] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+ dx[i]
            ny = y +dy[i]

            if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


input = sys.stdin.readline

n, m = map(int, input().split())

graph =[]
for i in range(n):
    graph.append(list(map(int, input().strip())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))

# git commit -m "code: Solve boj 02178 미로 탐색 (yeonju)"

