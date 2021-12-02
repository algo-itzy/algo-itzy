def dfs(x):
    if len(s) == m:
        print(*s)
        return

    for i in range(x, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()


n, m = map(int, input().split())
s = []

dfs(1)