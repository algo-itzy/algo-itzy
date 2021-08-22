def dfs(n, s):
    global res

    if n == N:
        res = min(res, s)

    if s > res:  # 불필요 연산 X -> 시간 초과 방지!!
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            dfs(n+1, s+arr[n][i])
            visit[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    res = 1000  # 최대로 초기화

    dfs(0, 0)
    print(f'#{tc}', res)


# 모든 경우의 수로 무식하게 풀었으나 시간초과
# 백트래킹이 답!
# 심지어 7-8번 return 없어도 시간 초과. 고난도