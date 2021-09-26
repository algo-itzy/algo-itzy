from collections import deque

D = ((1,0), (0,1), (-1,0), (0,-1))

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    visit = [[0] * m for _ in range(n)]

    q = deque()
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in D:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 'L' and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))

    print(f"#{tc}", sum(map(sum, visit)))
