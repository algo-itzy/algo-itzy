# 하다가... 이상한 거 같아서... 일단 ... 멈췄습니다...

def solution(m, n, board):
    answer = 0
    print(board)
    arr = [[0] * n for _ in range(m)]
    copy_arr = [[0] * n for _ in range(m)]

    print(arr)
    for i in range(len(board)):
        for j in range(len(board[i])):
            arr[i][j] = board[i][j]
            copy_arr[i][j] = board[i][j]

    for i in range(0, m-2):
        for j in range(0, n-2):
            if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1]:
                print('yes', i, j)
                copy_arr[i][j] = 'O'
                copy_arr[i][j+1] = 'O'
                copy_arr[i+1][j] = 'O'
                copy_arr[i+1][j+1] = 'O'
    print(copy_arr)
    li = []
    for j in range(n):
        tmp = []
        for i in range(m-1, -1, -1):
            if copy_arr[i][j] != 'O':
                tmp.append(copy_arr[i][j])

        li.append(tmp)
    print(li,'엘아이')
    for i in range(n):
        for j in range(n):
            if len(li[i]) < m:
                diff = m - len(li[i])



    return answer

solution(4,5, 	["CCBDE", "AAADE", "AAABF", "CCBBF"])

# def solution(m, n, board):
#
# solution(4,5, 	["CCBDE", "AAADE", "AAABF", "CCBBF"])
#

# git commit -m "code: Solve programmers 프렌즈4블록 (yeonju)"