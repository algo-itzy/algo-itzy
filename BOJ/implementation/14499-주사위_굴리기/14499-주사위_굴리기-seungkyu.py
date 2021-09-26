# git commit -m "code: Solve boj 14499 주사위 굴리기 (seungkyu)"
import sys
input = sys.stdin.readline

DIRS = ((), (0, 1), (0, -1), (-1, 0), (1, 0))
# 주사위 위(윗면), 북쪽, 동쪽, 서쪽, 남쪽, 아래(밑면)
dice = [0, 0, 0, 0, 0, 0]
N, M, x, y, K = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

cmds = list(map(int, input().split()))

for cmd in cmds:
    new_x = x + DIRS[cmd][0]
    new_y = y + DIRS[cmd][1]

    if 0<=new_x<N and 0<=new_y<M:
        # (index) 0:위, 1:북쪽, 2:동쪽, 3:서쪽, 4:남쪽, 5:아래
        if cmd == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif cmd == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif cmd == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        elif cmd == 4:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        if matrix[new_x][new_y] == 0:
            matrix[new_x][new_y] = dice[5]
        else:
            dice[5] = matrix[new_x][new_y]
            matrix[new_x][new_y] = 0

        x, y = new_x, new_y
        print(dice[0])
