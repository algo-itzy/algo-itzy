from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = deque()
    q.append((0, 0))
    a[0][0] = 1  # 시작점 int로

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and a[nx][ny] == '1':  # 방문 체크 없이
                a[nx][ny] = a[x][y] + 1
                q.append((nx, ny))


input = sys.stdin.readline
N, M = map(int, input().split())  # 줄, 미로
a = [list(input()) for _ in range(N)]  # str
bfs()

print("{}".format(a[N - 1][M - 1]))
