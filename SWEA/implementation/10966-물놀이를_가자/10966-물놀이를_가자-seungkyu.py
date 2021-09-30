# git commit -m "code: Solve swea 10966 물놀이를 가자 (seungkyu)"
from collections import deque

DIRS = ((0, 1),(-1, 0),(0, -1),(1, 0))

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dist = [[-1]*M for _ in range(N)]

    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 'L' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    ans = sum(map(sum, dist))

    print(f'#{tc} {ans}')
