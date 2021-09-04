from collections import deque

DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs():
    q = deque([(0, 0)])
    graph[0][0] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in DIRECTION:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                q.append((nr, nc))

    return graph[-1][-1]


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

print(bfs())
