from collections import deque

def bfs():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    q = deque()

    q.append((0, 0))
    visit[0][0] = 1

    while q:
        x, y = q.popleft()

        for d in D:
            nx, ny = x+d[0], y+d[1]
            
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                q.append([nx, ny])


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

bfs()

print(visit[-1][-1])