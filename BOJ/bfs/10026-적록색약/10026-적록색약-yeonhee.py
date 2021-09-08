import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(graph, r, c, color):
    q = deque([(r, c)])
    graph[r][c] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == color:
                q.append((nr, nc))
                graph[nr][nc] = 0


N = int(input())
graph = [list(input().strip()) for _ in range(N)]
# 적록색약 그래프
graph_rg = [['G' if color == 'R' else color for color in graph[r]] for r in range(N)]

result = 0
result_rg = 0

for r in range(N):
    for c in range(N):
        # 적록색약 아닌 사람
        if graph[r][c]:
            bfs(graph, r, c, graph[r][c])
            result += 1
        # 적록색약인 사람
        if graph_rg[r][c]:
            bfs(graph_rg, r, c, graph_rg[r][c])
            result_rg += 1

print(result, result_rg)

"""
오랜만에 극한의 한줄코딩 해봤습니다. (적록색약 그래프)
"""
