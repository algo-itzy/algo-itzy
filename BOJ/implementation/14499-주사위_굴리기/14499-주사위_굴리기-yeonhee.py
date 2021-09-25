import sys
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
dice = [0] * 6

for _ in range(K):
    d = int(cmd.pop(0))
    nx = x + dx[d-1]
    ny = y + dy[d-1]

    if 0 <= nx < N and 0 <= ny < M:

        if d == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif d == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif d == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        elif d == 4:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        if graph[nx][ny]:
            dice[5] = graph[nx][ny]
            graph[nx][ny] = 0
        else:
            graph[nx][ny] = dice[5]

        x, y = nx, ny
        print(dice[0])
