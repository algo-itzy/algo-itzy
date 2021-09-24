import sys
from collections import deque

sys.stdin = open('input.txt')

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    visited = [[-1]*M for _ in range(N)]
    q = deque()

    for r in range(N):
        row = input()
        for c in range(M):
            if row[c] == 'W':
                q.append((r, c))
                visited[r][c] = 0

    result = 0

    while q:
        r, c = q.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                result += visited[nr][nc]
                q.append((nr, nc))

    print(f'#{t} {result}')
