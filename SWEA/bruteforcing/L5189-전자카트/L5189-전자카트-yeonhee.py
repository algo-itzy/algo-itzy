import sys
sys.stdin = open('input.txt')


def dfs(cnt, curr, total):
    global result

    if cnt == n:
        total += graph[curr][0]
        result = min(result, total)
        return

    if total > result:
        return

    for i in range(1, n):
        if graph[curr][i] and not visited[i]:
            visited[i] = 1
            dfs(cnt+1, i, total + graph[curr][i])
            visited[i] = 0


for t in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    result = float('inf')
    dfs(1, 0, 0)

    print(f'#{t} {result}')
