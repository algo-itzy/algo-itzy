from collections import deque

moves = ((-1, 0), (1, 0), (0, 1), (0, -1))

def rotate(arr):
    return [list(i) for i in zip(*arr[::-1])]


def board_BFS(game_board, row, col, N):
    shapes = []
    q = deque([(row, col)])
    game_board[row][col] = 1

    while q:
        r, c = q.popleft()

        for y, x in moves:
            my = y + r
            mx = x + c

            if 0 <= mx < N and 0 <= my < N:
                if not game_board[my][mx]:
                    game_board[my][mx] = 1
                    q.append((my, mx))
                    shapes.append((my-row, mx-col))

    return shapes


def table_BFS(table, row, col, N):
    shape = []
    rollbacks = [(row, col)]
    q = deque([(row, col)])
    table[row][col] = 0

    while q:
        r, c = q.popleft()

        for y, x in moves:
            my = y + r
            mx = x + c

            if 0 <= mx < N and 0 <= my < N:
                if table[my][mx]:
                    table[my][mx] = 0
                    q.append((my, mx))
                    shape.append((my-row, mx-col))
                    rollbacks.append((my, mx))

    return shape, rollbacks


def compare(table, shape, N):
    for r in range(N):
        for c in range(N):
            if table[r][c]:
                puzzle, rollbacks = table_BFS(table, r, c, N)
                if puzzle == shape:
                    return len(rollbacks)
                else:
                    for y, x in rollbacks:
                        table[y][x] = 1


def solution(game_board, table):
    N = len(game_board)

    cnt = 0
    for row in range(N):
        for col in range(N):
            if not game_board[row][col]:
                shape = board_BFS(game_board, row, col, N)
                for _ in range(4):
                    check = compare(table, shape, N)
                    if check:
                        cnt+=check
                        break
                    table = rotate(table)

    return cnt 
    
# git commit -m "code: Solve programmers 퍼즐 조각 채우기 (yoonbaek)"