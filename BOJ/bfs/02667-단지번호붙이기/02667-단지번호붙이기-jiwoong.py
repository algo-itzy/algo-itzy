dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    global cnt
    visit[x][y] = 1
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and not visit[nx][ny]:
            dfs(nx, ny)


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]

ans = 1
visit = [[0] * N for _ in range(N)]
stack = []
for i in range(N):
    for j in range(N):
        if not visit[i][j] and arr[i][j] == 1:
            cnt = 0
            ans += 1
            dfs(i, j)
            stack.append(cnt)

print(ans - 1)
stack.sort()
for s in stack:
    print(s)
