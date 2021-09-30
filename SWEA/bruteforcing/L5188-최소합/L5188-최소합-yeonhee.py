import sys
sys.stdin = open('input.txt')

DIRECTIONS = ((0, 1), (1, 0))


def dfs(r, c):
    global result, tmp

    if result < tmp:
        return

    if r == c == n - 1 and result > tmp:
        result = tmp
        return

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if nr < n and nc < n and not visited[nr][nc]:
            visited[nr][nc] = 1
            tmp += graph[nr][nc]
            dfs(nr, nc)
            tmp -= graph[nr][nc]
            visited[nr][nc] = 0


for t in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = float('inf')
    visited = [[0] * n for _ in range(n)]
    tmp = graph[0][0]
    dfs(0, 0)
    print(f'#{t} {result}')
