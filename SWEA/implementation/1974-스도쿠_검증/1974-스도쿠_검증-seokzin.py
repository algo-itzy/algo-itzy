NUMSET = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def check():
    # 가로
    for i in range(9):
        if set(board[i]) != NUMSET:
            return 0

    # 세로
    for i in range(9):
        arr = []

        for j in range(9):
            arr.append(board[j][i])
        
        if set(arr) != NUMSET:
            return 0

    # 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):    
            arr = []

            arr += board[i][j:j+3]  # extend 역할을 하는 +
            arr += board[i+1][j:j+3]
            arr += board[i+2][j:j+3]

            if set(arr) != NUMSET:
                return 0

    return 1


T = int(input())

for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]

    print(f"#{tc}", check())