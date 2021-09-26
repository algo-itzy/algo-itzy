def dfs(x, y, r, d, s):  # 우, 하 횟수,
    global res

    if s >= res:
        return

    s += arr[y][x]

    if r+d == 2*(n-1):
        res = min(res, s)

    else:
        if r < n-1:
            dfs(x+1, y, r+1, d, s)

        if d < n-1:
            dfs(x, y+1, r, d+1, s)


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 9999

    dfs(0, 0, 0, 0, 0)

    print(f'#{tc}', res)

# 우, 하 이동 횟수가 n-1 로 고정되어있어 가능한 풀이
# s >= res시 break 없으면 시간 초과