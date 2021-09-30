def dfs(x, s, visit):
    global res

    if s >= res:
        return

    if visit == (1<<n) - 1:
        res = min(res, s+arr[x][0])  # 마지막 돌아오는 비용 더한 뒤 비교
        return

    for i in range(1, n):
        if not visit & (1<<i):
            dfs(i, s+arr[x][i], visit|(1<<i))


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    res = 1000

    dfs(0, 0, 1)
    print(f"#{tc}", res)

# 이걸 왜 비트마스크로 풀려 했을까.. 고생 했습니다.