import sys
sys.stdin = open('input.txt')

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dfs(r, c, k):
    global result
    result = max(result, visited[r][c])

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if mountain[r][c] > mountain[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                dfs(nr, nc, k)
                visited[nr][nc] = 0
            elif k and mountain[r][c] > mountain[nr][nc] - k:
                tmp = mountain[nr][nc]
                mountain[nr][nc] = mountain[r][c] - 1
                visited[nr][nc] = visited[r][c] + 1
                dfs(nr, nc, 0)
                mountain[nr][nc] = tmp
                visited[nr][nc] = 0


for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    top = max(sum(mountain, []))

    for r in range(N):
        for c in range(N):
            if mountain[r][c] == top:
                visited[r][c] = 1
                dfs(r, c, K)
                visited[r][c] = 0

    print(f'#{t} {result}')
