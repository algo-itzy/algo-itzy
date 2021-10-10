# git commit -m "code: Solve swea L5250 최소 비용 (seungkyu)"
import sys
from collections import deque
sys.stdin = open('input.txt')

DIRS = ((0, 1),(0, -1),(1, 0),(-1, 0))


def bfs(x, y):
    q = deque([(x, y)])
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                fuel = 0
                if mat[x][y] < mat[nx][ny]:
                    fuel = mat[nx][ny] - mat[x][y]
                if dist[nx][ny] > dist[x][y] + fuel + 1:
                    dist[nx][ny] = dist[x][y] + fuel + 1
                    q.append((nx, ny))
    
    return dist[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf')]*N for _ in range(N)]

    ans = bfs(0, 0)

    print(f'#{tc} {ans}')
