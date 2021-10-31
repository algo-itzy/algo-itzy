# git commit -m "code: Solve programmers 프렌즈4블록 (seungkyu)"
def break_find(m, n, board):
    break_set = set()
    
    for i in range(n):
        for j in range(m):
                cur = board[i][j]
                if cur != -1:
                    if i < n-1 and j < m-1:
                        if board[i+1][j] == cur and board[i][j+1] == cur and board[i+1][j+1] == cur:
                            break_set.add((i, j))
                            break_set.add((i+1, j))
                            break_set.add((i, j+1))
                            break_set.add((i+1, j+1))
                            
    for x, y in break_set:
        board[x][y] = 0
        
    for i, row in enumerate(board):
        empty = row.count(0)
        tmp = []
        for v in row:
            if v!= 0:
                tmp.append(v)
        board[i] = [-1]*empty + tmp

    return len(break_set)

    
def solution(m, n, board):
    cnt = 0
    board = list(map(list, zip(*board)))
    
    while True:
        break_block_num = break_find(m, n, board)
        if break_block_num:
            cnt += break_block_num
            continue
        else:
            break
    return cnt
