from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    cnt = 0
    Q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:  # 익었으면
                    Q.append((i, j, k))
    while len(Q) != 0:
        tx, ty, tz = Q.popleft()
        for i in range(6):
            dx = tx + matrix[i][0]
            dy = ty + matrix[i][1]
            dz = tz + matrix[i][2]
            if 0 <= dx < H and 0 <= dy < N and 0 <= dz < M:  # 상자 내부
                if arr[dx][dy][dz] == 0:  # 안 익었으면
                    Q.append((dx, dy, dz))
                    arr[dx][dy][dz] = arr[tx][ty][tz] + 1
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] > cnt:
                    cnt = arr[i][j][k]
                elif arr[i][j][k] == 0:  # 안 익었으면
                    return -1
    return cnt - 1


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
matrix = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1]]
ans = bfs()
print(ans)
