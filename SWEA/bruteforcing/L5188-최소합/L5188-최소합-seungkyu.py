# git commit -m "code: Solve swea L5188 최소합 (seungkyu)"
DIRECTIONS = ((0, 1),(1, 0))


def dfs(x, y):
    global res, cnt
    visited = [[0]*N for _ in range(N)]
    if res < cnt: 
        return
    if x == N-1 and y == N-1:
        res = cnt
        return
    for dx, dy in DIRECTIONS:
        nx = x + dx
        ny = y + dy
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            visited[nx][ny] = 1
            cnt += matrix[nx][ny]
            dfs(nx, ny)
            cnt -= matrix[nx][ny]  
            visited[nx][ny] = 0

    return visited[N-1][N-1]


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    res = float('inf')
    cnt = matrix[0][0]
    dfs(0, 0)
    print(f'#{tc} {res}')
