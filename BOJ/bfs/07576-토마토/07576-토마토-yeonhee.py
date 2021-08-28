from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs():
    q = deque()

    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 1:
                q.append([r, c])

    while q:
        r, c = q.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not tomatoes[nr][nc]:
                tomatoes[nr][nc] = tomatoes[r][c] + 1
                q.append([nr, nc])


M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

bfs()

flag = False
result = -2

for row in tomatoes:
    for tomato in row:
        if not tomato:
            flag = True
        result = max(result, tomato)

if flag:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)
