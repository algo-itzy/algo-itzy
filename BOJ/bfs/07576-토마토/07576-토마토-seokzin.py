from collections import deque

def bfs():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append([i, j])

    while q:
        x, y = q.popleft()

        for d in D:
            nx, ny = x+d[0], y+d[1]
            
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

bfs()

res = max(map(max, arr)) - 1

for row in arr:
    for x in row:
        if x == 0:
            res = - 1

print(res)