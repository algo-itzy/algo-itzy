from collections import deque

M, N = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if all(0 not in arr for arr in a):
    print(0)

else:
    deq = deque()
    for i in range(N):
        for j in range(M):
            if a[i][j] == 1:
                deq.append((i, j))

    while deq:
        x, y = deq.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and a[nx][ny] == 0:
                a[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1
                deq.append((nx, ny))

    if any(0 in arr for arr in a):
        print(-1)
    else:
        print(max(map(max, visited)))
