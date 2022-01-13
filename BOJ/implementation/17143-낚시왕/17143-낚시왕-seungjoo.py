# git commit -m "code: Solve boj 17143 낚시왕 (seungjoo)"
import sys
input = sys.stdin.readline

def move_shark():
    new_board = [[0 for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if not board[x][y]:
                continue
            t_x, t_y = x, y
            s, d, z = board[t_x][t_y]
            total = s
            if d == 0 or d == 1:
                s %= 2 * R - 2
                while s:
                    if (t_x == R - 1 and d == 1) or (t_x == 0 and d == 0):
                        d ^= 1 
                    nx = t_x + delta[d][0]
                    s -= 1
                    t_x = nx
            else:
                s %= 2 * C - 2
                while s:
                    if (t_y == C - 1 and d == 2) or (t_y == 0 and d == 3):
                        d = (d - 2)^1 + 2
                    ny = t_y + delta[d][1]
                    s -= 1
                    t_y = ny
            if new_board[t_x][t_y] and new_board[t_x][t_y][2] > z:
                pass
            else:
                new_board[t_x][t_y] = (total, d, z)
    return new_board

R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = (s, d - 1, z)

delta = ((-1, 0), (1, 0), (0, 1), (0, -1))
answer = 0
# 낚시왕은 1초당 1열씩 이동
for king_of_fishing in range(C):
    for i in range(R):
        if board[i][king_of_fishing]:
            answer += board[i][king_of_fishing][2]
            board[i][king_of_fishing] = 0
            break
    board = move_shark()
# 해당 열에서 가장 가까운 상어를 잡는다. 잡으면 상어는 사라진다.
# 상어들이 이동한다.
print(answer)