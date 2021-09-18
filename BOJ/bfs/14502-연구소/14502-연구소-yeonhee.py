import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def set_wall(w):
    global result
    if w == 3:
        # virus
        visited = [[0]*m for _ in range(n)]
        virus = deque(virus_origin)

        for r, c in virus:
            visited[r][c] = 1
        while virus:
            r, c = virus.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and not lab[nr][nc]:
                    visited[nr][nc] = 1
                    virus.append((nr, nc))

        # safety zone
        cnt = 0
        for r in range(n):
            for c in range(m):
                if not lab[r][c] and not visited[r][c]:
                    cnt += 1
        result = max(result, cnt)
        return

    # set wall recursively
    for r in range(n):
        for c in range(m):
            if not lab[r][c]:
                lab[r][c] = 1
                set_wall(w + 1)
                lab[r][c] = 0


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
virus_origin = []

for r in range(n):
    for c in range(m):
        if lab[r][c] == 2:
            virus_origin.append((r, c))

result = 0
set_wall(0)
print(result)
