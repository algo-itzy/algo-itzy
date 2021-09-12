import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def bfs():
    q = deque()

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomatoes[z][y][x] == 1:
                    q.append([x, y, z])

    while q:
        x, y, z = q.popleft()
        for dx, dy, dz in DIRECTIONS:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and not tomatoes[nz][ny][nx]:
                tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
                q.append([nx, ny, nz])


M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

bfs()

flag = 1
result = -1

for z in tomatoes:
    for y in z:
        for x in y:
            if not x:
                flag = 0
            result = max(result, x)

if not flag:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result-1)


"""
7576 문제를 그냥 3차원으로 바꿨습니다.
"""
