
def DFS(row,sum_nums):
    global min_sum
    if row == N:
        min_sum = min(min_sum,sum_nums)
        return
    if sum_nums > min_sum:
        return
    for i in range(N):
        if not col_check[i]:
            col_check[i] = True
            DFS(row+1,sum_nums+matrix[row][i])
            col_check[i] = False


for test in range(1,int(input())+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    min_sum = float('inf')
    col_check = [False] * N
    DFS(0,0)
    print(f'#{test} {min_sum}')