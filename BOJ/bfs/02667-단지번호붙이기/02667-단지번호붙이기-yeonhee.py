from collections import deque

DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(a, b):
    q = deque([(a, b)])
    graph[a][b] = 0
    cnt = 1

    while q:
        r, c = q.popleft()
        for dr, dc in DIRECTION:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc]:
                graph[nr][nc] = 0
                q.append((nr, nc))
                cnt += 1
    return cnt


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

result = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            result.append(bfs(r, c))

print(len(result), *sorted(result), sep='\n')
