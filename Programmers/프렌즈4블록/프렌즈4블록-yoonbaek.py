def solution(m, n, board):
    cnt = 0
    board = [[char for char in word] for word in board]

    def explode():
        exp_set = set()
        for row in range(m-1):
            for col in range(n-1):
                if board[row][col] and board[row][col] == board[row][col+1] == board[row+1][col] == board[row+1][col+1]:
                    exp_set.add((row, col)) 
                    exp_set.add((row, col+1)) 
                    exp_set.add((row+1, col))
                    exp_set.add((row+1, col+1))
        
        for row, col in exp_set:
            board[row][col] = 0

        return len(exp_set)
    

    def gravity():
        stack = []
        for col in range(n):
            for row in range(m):
                if board[row][col]:
                    stack.append(board[row][col])
                    board[row][col] = 0
            while stack:
                board[row][col] = stack.pop()
                row -= 1

    while 1:
        blocks = explode()
        if not blocks:
            break
        cnt += blocks
        gravity()

    return cnt

m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]# 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(m, n, board)



# git commit -m "code: Solve programmers 프렌즈4블록 (yoonbaek)"  