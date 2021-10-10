# git commit -m "code: Solve swea L5209 최소 생산 비용 (seungkyu)"
import sys
sys.stdin = open('input.txt')


def dfs(x, tot):
    global res

    if tot > res:
        return

    if x == N:
        res = min(tot, res)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(x+1, tot+mat[x][j])
            visited[j] = 0
    

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [0]*N
    res = 100*N
    dfs(0, 0)
    
    print(f'#{tc} {res}')
