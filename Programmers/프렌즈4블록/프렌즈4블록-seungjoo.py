# git commit -m "code: Solve programmers 프렌즈4블록 (seungjoo)"

def bomb_block(b, m, n):
    block = set()
    for i in range(m - 1):
        for j in range(n - 1):
            if b[i][j] and b[i][j] == b[i][j + 1] == b[i + 1][j] == b[i + 1][j + 1]:
                for dx, dy in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                    nx, ny = i + dx, j + dy
                    block.add((nx, ny))
    if not block:
        return 0, 0
    for x, y in block:
        b[x][y] = 0
    new_board = [[0] * n for _ in range(m)]
    for j in range(n):
        idx = m - 1
        for i in range(m - 1, -1, -1):
            if b[i][j]:
                new_board[idx][j] = b[i][j]
                idx -= 1
    return new_board, len(block)
     
def solution(m, n, board):
    board = [list(row) for row in board]
    count = 0
    while board:
        board, cnt = bomb_block(board, m, n)
        count += cnt
    return count

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))