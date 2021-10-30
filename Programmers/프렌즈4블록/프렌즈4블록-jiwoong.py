# git commit -m "code: Solve programmers 프렌즈4블록 (jiwoong)"
def solution(m, n, board):
    answer = 0

    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        arr = [[0] * n for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    arr[i][j], arr[i][j + 1], arr[i + 1][j], arr[i + 1][j + 1] = 1, 1, 1, 1
        cnt = 0

        for i in range(m):
            cnt += sum(arr[i])
        answer += cnt

        if cnt == 0:
            break

        for i in range(m - 1, -1, -1):
            for j in range(n):
                if arr[i][j] == 1:
                    x = i - 1
                    while x >= 0 and arr[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        arr[x][j] = 1
    return answer