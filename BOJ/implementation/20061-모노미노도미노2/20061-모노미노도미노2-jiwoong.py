from collections import deque
import sys

input = sys.stdin.readline


def domino(board, blocks):
    ans = 0
    for b in blocks:
        [check, y] = b
        board.append([1 for _ in range(4)])
        for i in range(2, 7):
            if check == 2 and board[i][y] == 0 and board[i][y + 1] == 0:
                continue
            elif check != 2 and board[i][y] == 0:
                continue

            board[i - 1][y] = 1
            if check == 2:
                board[i - 1][y + 1] = 1
            elif check == 3:
                board[i - 2][y] = 1
            break
        board.pop()

        row = -1
        while row >= -4:
            if sum(board[row]) < 4:
                row -= 1
                continue
            ans += 1
            del board[row]
            board.appendleft([0 for _ in range(4)])
        while sum(board[1]) > 0:
            board.pop()
            board.appendleft([0 for _ in range(4)])
    return ans


if __name__ == '__main__':
    n = int(input())
    green, blue = [], []
    for _ in range(n):
        t, x, y = map(int, input().split())
        green.append([t, y])
        if t == 2:
            t = 3
        elif t == 3:
            t = 2
        blue.append([t, x])

    g = deque([[0 for _ in range(4)] for _ in range(6)])
    b = deque([[0 for _ in range(4)] for _ in range(6)])
    ans = 0
    ans += domino(g, green)
    ans += domino(b, blue)

    cnt = 0
    cnt += sum([sum(b_row) for b_row in b])
    cnt += sum([sum(g_row) for g_row in g])

    print(ans)
    print(cnt)