# git commit -m "code: Solve swea L5250 최소 비용 (seungjoo)"
from heapq import heappush, heappop

def dijkstra(x, y):
    heap = []
    dists[x][y] = 0
    heappush(heap, (0, 0, 0))
    while heap:
        cur_dist, x, y = heappop(heap)
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                cost = max(0, matrix[nx][ny] - matrix[x][y]) + 1
                next_dist = cur_dist + cost
                if dists[nx][ny] > next_dist:
                    dists[nx][ny] = next_dist
                    heappush(heap, (next_dist, nx, ny))


for test in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for __ in range(N)]
    dists = [[float('inf')] * N for __ in range(N)]

    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dijkstra(0, 0)
    
    print(f'#{test} {dists[N-1][N-1]}')