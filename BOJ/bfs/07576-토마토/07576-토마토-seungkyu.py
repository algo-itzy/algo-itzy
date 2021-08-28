from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 이동한 곳이 범위를 벗어나지 않고, 익지않은 토마토일때
            if 0 <= new_x < N and 0 <= new_y < M and matrix[new_x][new_y] == 0:
                matrix[new_x][new_y] = matrix[x][y] + 1
                queue.append((new_x, new_y))


def check():
    ans = 0
    for row in matrix:
        for i in row:
            if i == 0:
                print(-1)
                return
        ans = max(ans, max(row))
    print(ans-1)

queue = deque()
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append((i, j))

bfs()
check()
