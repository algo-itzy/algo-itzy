import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

bfs()

flag = 0
max_cnt = -2
for i in range(N):
    for j in range(M):
        if not matrix[i][j]:
            flag = 1
        max_cnt = max(max_cnt, matrix[i][j])
if flag:
    print(-1)
elif max_cnt == -1:
    print(0)
else:
    print(max_cnt - 1)