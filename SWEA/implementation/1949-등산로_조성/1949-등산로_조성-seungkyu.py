# git commit -m "code: Solve swea 1949 등산로 조성 (seungkyu)"
import sys
sys.stdin = open('input.txt')

DIRS = ((-1, 0),(1, 0),(0, -1),(0, 1))

# 현재 위치 들고 다니지 않을 때
def dfs(x, y, road, skill):
    global ans

    if road > ans:
        ans = road

    visited[x][y] = 1

    for dx, dy in DIRS:
        nx = x + dx
        ny = y + dy

        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            if matrix[x][y] > matrix[nx][ny]:
                dfs(nx, ny, road+1, skill)
            elif skill and matrix[x][y] > matrix[nx][ny] - K:
                tmp = matrix[nx][ny]
                matrix[nx][ny] = matrix[x][y] - 1
                dfs(nx, ny, road+1, 0)
                matrix[nx][ny] = tmp
    visited[x][y] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]    
    max_h = 0

    for i in range(N):
        for j in range(N):
            if max_h < matrix[i][j]:
                max_h = matrix[i][j]

    visited = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_h:
                dfs(i, j, 1, 1)
    
    print(f'#{tc} {ans}')
