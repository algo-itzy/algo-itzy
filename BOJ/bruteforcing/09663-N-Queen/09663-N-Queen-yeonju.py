def nqueen(queen, row):
    global res

    if n == row: # 마지막 행까지 오는 데 성공했으면 
        res += 1
        return

    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row] or abs(queen[row] - queen[i]) == row - i: # 같은 열 or 대각선에 퀸 있으면 break, 
                break
        else:
            nqueen(queen, row + 1) # 바로 위의 for 문에 안 걸리면, 그 다음 열 체크하러 내려감


n = int(input())
res = 0
nqueen([0] * n, 0)  # 1차원 배열 선언 -> 같은 행에 퀸이 오는 문제는 처리 가능 
print(res)

# git commit -m "code: Solve boj 09663 N-Queen (yeonju)"