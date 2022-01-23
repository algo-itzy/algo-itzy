# git commit -m "code: Solve boj 17837 새로운 게임2 (seungjoo)"
import sys
input = sys.stdin.readline

def move_white(x, y, nx, ny):
    now = chess[x][y].index(coin)
    top = len(chess[x][y])
    for i in range(now, top):
        coins[chess[x][y][i]][0] = nx
        coins[chess[x][y][i]][1] = ny
        chess[nx][ny].append(chess[x][y][i])
    for _ in range(top - now):
        chess[x][y].pop()


def move_red(x, y, nx, ny):
    now = chess[x][y].index(coin)
    top = len(chess[x][y])
    for i in range(top - 1, now - 1, -1):
        coins[chess[x][y][i]][0] = nx
        coins[chess[x][y][i]][1] = ny
        chess[nx][ny].append(chess[x][y][i])
    for _ in range(top - now):
        chess[x][y].pop()


N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]
coins = {}
delta = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))
for i in range(K):
    x, y, d = map(int, input().split())
    chess[x - 1][y - 1].append(i)
    coins[i] = [x - 1, y - 1, d]

for turn in range(1, 1001):
    for coin in range(K):
        x, y, d = coins[coin]
        nx, ny = x + delta[d][0], y + delta[d][1]
        if 0 <= nx < N and 0 <= ny < N  and color[nx][ny] != 2:
            if color[nx][ny] == 0:
                move_white(x, y, nx, ny)
            else:
                move_red(x, y, nx, ny)
        else:
            if d == 1 or d == 2:
                d = ((d - 1)^1) + 1
            else:
                d = ((d - 3)^1) + 3
            coins[coin][2] = d
            nx, ny = x + delta[d][0], y + delta[d][1]
            if 0 <= nx < N and 0 <= ny < N  and color[nx][ny] != 2:
                if color[nx][ny] == 0:
                    move_white(x, y, nx, ny)
                else:
                    move_red(x, y, nx, ny)
        
        if 0 <= nx < N and 0 <= ny < N  and len(chess[nx][ny]) >= 4:
            print(turn)
            exit()
            
print(-1)