import sys
sys.stdin = open('input.txt')


def dfs(r, total):
    global result

    if r == N:
        if result > total:
            result = total
        return

    if result < total:
        return

    for c in range(N):
        if not visited[c]:
            visited[c] = 1
            dfs(r+1, total + data[r][c])
            visited[c] = 0


for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = float('inf')
    dfs(0, 0)
    print(f'#{t} {result}')
