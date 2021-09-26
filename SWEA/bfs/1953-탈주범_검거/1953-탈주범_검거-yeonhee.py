import sys
from collections import deque

sys.stdin = open('input.txt')

DIRECTIONS = [
    (),
    ((1, 0), (0, 1), (-1, 0), (0, -1)),
    ((1, 0), (-1, 0)),
    ((0, 1), (0, -1)),
    ((-1, 0), (0, 1)),
    ((1, 0), (0, 1)),
    ((1, 0), (0, -1)),
    ((-1, 0), (0, -1))
]

for t in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    result = 1

    q = deque([(R, C)])

    while q:
        r, c = q.popleft()
        for dr, dc in DIRECTIONS[tunnel[r][c]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if (-dr, -dc) in DIRECTIONS[tunnel[nr][nc]]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                    if visited[nr][nc] <= L:
                        result += 1

    print(f'#{t} {result}')
