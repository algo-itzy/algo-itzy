# git commit -m "code: Solve boj 02206 벽 부수고 이동하기 (seungkyu)"
import sys
from collections import deque
input = sys.stdin.readline

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

def bfs(x, y):
    q = deque()
    q.append((x, y, 1))
    dist[x][y][1] = 1

    while q:
        x, y, skill = q.popleft()

        if x == N-1 and y == M-1:
            return dist[N-1][M-1][skill]

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<M:
                if mat[nx][ny] == 0:
                    if not dist[nx][ny][skill]:
                        dist[nx][ny][skill] = dist[x][y][skill] + 1
                        q.append((nx, ny, skill))
                elif mat[nx][ny] == 1:
                    if skill == 1:
                        dist[nx][ny][0] = dist[x][y][1] + 1
                        q.append((nx, ny, 0))

    return -1


N, M = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(N)]
# 방문 배열을 2개로 만들어서 구분해줘야 맞게 나옴..
dist = [[[0]*2 for _ in range(M)] for _ in range(N)]
ans = bfs(0, 0)
if ans > 0:
    print(ans)
else:
    print(-1)