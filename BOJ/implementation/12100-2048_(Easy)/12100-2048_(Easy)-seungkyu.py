# git commit -m "code: Solve boj 12100 2048 (Easy) (seungkyu)"
import sys
input = sys.stdin.readline


def right(board, n):
    for row in board:
        end = n-1
        for i in range(n-2, -1, -1):
            if row[i]:
                tmp = row[i]
                row[i] = 0
                if row[end] == 0:
                    row[end] = tmp
                elif row[end] == tmp:
                    row[end] *= 2
                    end -= 1
                else:
                    end -= 1
                    row[end] = tmp
    return board


def left(board, n):
    for row in board:
        end = 0
        for i in range(1, n):
            if row[i]:
                tmp = row[i]
                row[i] = 0
                if row[end] == 0:
                    row[end] = tmp
                elif row[end] == tmp:
                    row[end] *= 2
                    end += 1
                else:
                    end += 1
                    row[end] = tmp
    return board


def up(board, n):
    board_t = transpose(board)
    board_t = left(board_t, n)
    return transpose(board_t)


def down(board, n):
    board_t = transpose(board)
    board_t = right(board_t, n)
    return transpose(board_t)


def transpose(board):
    board_t = list(zip(*board))
    tmp = []
    for row in board_t:
        tmp.append(list(row))
    return tmp


def copy_board(board):
    return [row[:] for row in board]


def dfs(board, cnt):
    ans = 0
    if cnt == 5:
        for row in board:
            ans = max(ans, max(row))
        return ans
    else:
        return max(dfs(up(copy_board(board), n), cnt+1), 
                    dfs(down(copy_board(board), n), cnt+1),
                    dfs(left(copy_board(board), n), cnt+1),
                    dfs(right(copy_board(board), n), cnt+1))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = dfs(board, 0)
print(ans)
