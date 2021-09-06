from collections import deque

D = ((1,0), (-1,0), (0,1), (0,-1))


def bfs(a, b):
    q = deque()
    
    q.append([a, b])
    visit[a][b] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == arr[x][y] and not visit[nx][ny]:
                    q.append([nx, ny])
                    visit[nx][ny] = 1


n = int(input())
arr = [list(input()) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
cnt = [0, 0]

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i, j)
            cnt[0] += 1

visit = [[0]*n for _ in range(n)] # 초기화

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i, j)
            cnt[1] += 1

print(*cnt)

# 더 개선할 수 없었을까 아쉽