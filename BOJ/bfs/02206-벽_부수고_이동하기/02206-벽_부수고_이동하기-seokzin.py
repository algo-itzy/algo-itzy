from collections import deque

D = ((1, 0), (-1, 0), (0, -1), (0, 1))


def bfs():
    q.append([0, 0, 0])
    visit[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        for dx, dy in D:
            nx, ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visit[nx][ny][z] == -1:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    q.append([nx, ny, z])
                elif z == 0 and arr[nx][ny] == 1 and visit[nx][ny][z+1] == -1:
                    visit[nx][ny][z+1] = visit[x][y][z] + 1
                    q.append([nx, ny, z+1])


n, m = map(int, input().split())
visit = [[[-1]*2 for _ in range(m)] for _ in range(n)]
q = deque()
arr = [list(map(int, input())) for _ in range(n)]
res = visit[-1][-1]

bfs()

if res[0] == -1:
    print(res[1])
elif res[1] == -1:
    print(res[0])
else:
    print(min(res))