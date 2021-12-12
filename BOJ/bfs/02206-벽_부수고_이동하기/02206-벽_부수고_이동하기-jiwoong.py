# git commit -m "code: Solve boj 02206 벽 부수고 이동하기 (jiwoong)"
import sys
from collections import deque

input = sys.stdin.readline

dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs(x, y, broken):
    q = deque()
    q.append((x, y, broken))
    visited[x][y][broken] = 1

    while q:
        cx, cy, br = q.popleft()
        if cx == N - 1 and cy == M - 1:
            return visited[N - 1][M - 1][br]
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 0이라면 벽을 부실 필요 없음
                if arr[nx][ny] == 0 and not visited[nx][ny][br]:
                    q.append((nx, ny, br))
                    visited[nx][ny][br] = visited[cx][cy][br] + 1
                # 1이고 벽을 부시지 않은 상태라면 벽을 부시고 지나감
                if arr[nx][ny] == 1 and not br:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[cx][cy][0] + 1
    return -1


N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, list(input().rstrip()))))
# 벽을 부신 상태인지 아닌지를 나타내도록 함
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(bfs(0, 0, 0))
