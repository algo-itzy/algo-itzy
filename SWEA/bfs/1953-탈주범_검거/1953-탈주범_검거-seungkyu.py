# git commit -m "code: Solve swea 1953 탈주범 검거 (seungkyu)"
from collections import deque

DIRS = ((0, 1),(1, 0),(0, -1),(-1, 0))  #우하좌상
PIPES = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
    ]


T = int(input())
for tc in range(1, T+1):

    N, M, x, y, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    q = deque([(x, y)])
    visited[x][y] = 1

    ans = 0
    while q:
        x, y = q.popleft()
        ans += 1
        if visited[x][y] >= L: continue

        for idx, (dx, dy) in enumerate(DIRS):
            cur = tunnel[x][y]
            if PIPES[cur][idx] == 0: continue

            nx, ny = x+dx, y+dy

            if nx<0 or nx>=N or ny<0 or ny>=M: continue

            nd = (idx+2)%4
            np = tunnel[nx][ny]

            if visited[nx][ny] or PIPES[np][nd] == 0: continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

    print(f'#{tc} {ans}')
