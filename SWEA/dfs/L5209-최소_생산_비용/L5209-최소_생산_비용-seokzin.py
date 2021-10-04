def dfs(x, s, visit):
    global res

    if res < s:
        return

    if visit == (1<<n) - 1:
        res = s
        return


    for i in range(n):
        if not visit & (1<<i):
            dfs(x+1, s+arr[x][i], visit|(1<<i))


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = float('inf')

    dfs(0, 0, 0)
    print(f'#{tc}', res)
