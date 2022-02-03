import sys

input = sys.stdin.readline

directions = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

n, m = map(int, input().split())

square = [list(map(int, input().split())) for _ in range(n)]
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
diagonals = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

# 이동 정보- d 번 방향으로 s 칸 이동
for _ in range(m):
    moved_clouds = []
    cnt_list = []
    d, s = map(int, input().split())

    for x, y in clouds:
        nx, ny = (x + directions[d][0] * s) % n, (y + directions[d][1] * s) % n
        square[nx][ny] += 1
        moved_clouds.append((nx,ny))

    for moved_cloud in moved_clouds:
        x, y = moved_cloud
        cnt = 0
        for i in range(4):
            nx, ny = x + diagonals[i][0], y + diagonals[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if square[nx][ny] > 0:
                    cnt += 1
        cnt_list.append(cnt)

    for i in range(len(moved_clouds)):
        x, y = moved_clouds[i]
        square[x][y] += cnt_list[i]

    clouds = []
    for i in range(n):
        for j in range(n):
            if (i,j) not in moved_clouds:
                if square[i][j] >= 2:
                    square[i][j] -= 2
                    clouds.append((i, j))

total = 0
for i in range(n):
    for j in range(n):
        total += square[i][j]

print(total)


# git commit -m "code: Solve boj 21610 마법사 상어와 비바라기 (yeonju)"