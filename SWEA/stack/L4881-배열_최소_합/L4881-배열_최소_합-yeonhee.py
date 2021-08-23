import sys
sys.stdin = open('input.txt')


def dfs(r):  # row
    global tmp, result

    if tmp > result:
        return

    if r == n:
        if tmp < result:
            result = tmp
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            tmp += arr[r][i]
            dfs(r+1)
            visited[i] = 0
            tmp -= arr[r][i]


for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    tmp, result = 0, 1000
    dfs(0)
    print(f'#{t} {result}')
