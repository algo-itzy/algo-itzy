# git commit -m "code: Solve swea L5209 최소 생산 비용 (jiwoong)"
def dfs(i, total):  # 행, 현재 타임 합
    global ans
    if total >= ans:
        return
    if i == N:
        ans = min(total, ans)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(i + 1, total + V[i][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [0] * N  # 열체크
    dfs(0, 0)
    print("#{} {}".format(tc, ans))
