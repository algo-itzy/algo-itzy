import sys
from collections import deque
sys.stdin = open('input.txt')


DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(sr, sc):
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                tmp = 1
                if graph[nr][nc] > graph[r][c]:
                    tmp += graph[nr][nc] - graph[r][c]
                if dist[nr][nc] > dist[r][c] + tmp:
                    dist[nr][nc] = dist[r][c] + tmp
                    q.append((nr, nc))


for t in range(1, int(input())+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf')]*N for _ in range(N)]
    dist[0][0] = 0
    bfs(0, 0)
    print(f'#{t} {dist[-1][-1]}')
