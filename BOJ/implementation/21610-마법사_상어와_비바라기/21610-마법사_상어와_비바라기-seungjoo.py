# git commit -m "code: Solve boj 21610 마법사 상어와 비바라기 (seungjoo)"
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]
delta = ((0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
check = ((-1, 1), (1, 1), (-1, -1), (1, -1))
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for d, s in moves:
    # 구름 이동
    moved_clouds = set()
    for _ in range(len(clouds)):
        x, y = clouds.pop()
        nx, ny = (x + delta[d][0] * s) % N, (y + delta[d][1] * s) % N
        # 구름에서 비내림
        A[nx][ny] += 1
        moved_clouds.add((nx, ny))
    for x, y in moved_clouds:
        tmp = 0
        for dx, dy in check:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N  and 0 <= ny < N and A[nx][ny]:
                tmp += 1
        A[x][y] += tmp
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in moved_clouds:
                A[i][j] -= 2
                clouds.append((i, j))
water = 0
for i in range(N):
    for j in range(N):
        water += A[i][j]
print(water)