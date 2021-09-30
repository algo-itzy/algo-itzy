# git commit -m "code: Solve swea L5189 전자카트 (seungkyu)"
def dfs(x, cnt, tot):
    global res

    if tot > res:
        return
    if cnt == N:
        tot += mat[x][0]
        if tot < res:
            res = tot
            return

    for i in range(1, N):
        if mat[x][i] and not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1, tot+mat[x][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    visited = [0 for _ in range(N)]
    res = 100*N
    
    dfs(0, 1, 0)
    print(f'#{tc} {res}')
