# git commit -m "code: Solve boj 12100 2048 (Easy) (seungjoo)"
import sys
input = sys.stdin.readline

def next_turn(time, board):
    if time == 5:
        return
    for d in range(4):
        new_board = rotate_board(board, d)
        next_turn(time + 1, new_board)


def rotate_board(matrix, direction):
    global answer
    ret = [[0] * N for _ in range(N)]
    if direction == 0:
        for row in range(N):
            for col in range(N):
                ret[col][N - 1 - row] = matrix[row][col]
    elif direction == 1:
        for row in range(N):
            for col in range(N):
                ret[N - 1 - col][N - 1 - row] = matrix[row][col]
    elif direction == 2:
        for row in range(N):
            for col in range(N):
                ret[N - 1 - col][row] = matrix[row][col]
    else:
        for row in range(N):
            for col in range(N):
                ret[row][col] = matrix[row][col]
    ret_mat = [[0] * N for _ in range(N)]
    for j in range(N):
        tmp = []
        fin = []
        for i in range(N):
            if ret[i][j]:
                if not tmp:
                    tmp.append(ret[i][j])
                else:
                    if tmp[-1] == ret[i][j]:
                        tmp.pop()
                        fin.append(ret[i][j] * 2)
                        answer = max(answer, ret[i][j] * 2)
                    else:
                        fin.append(tmp.pop())
                        tmp.append(ret[i][j])
        if tmp:
            fin.append(tmp.pop())
        if not fin:
            continue
        start = 0
        for row in range(len(fin)):
            ret_mat[row][j] = fin[start]
            start += 1
    return ret_mat


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 최대 5번 이동해서 가장 큰 블록의 값.
next_turn(0, board)
print(answer)