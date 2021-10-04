def dfs(x, cnt):
    global res

    if res < cnt:
        return

    if x >= n:
        res = cnt
        return

    for i in range(arr[x-1], 0, -1):  # 역탐색 중요
        dfs(x+i, cnt+1)


for tc in range(1, int(input())+1):
    n, *arr = list(map(int, input().split()))
    res = float('inf')
    dfs(1, -1)  # 출발은 카운팅 X라서 -1 시작

    print(f'#{tc}', res)
