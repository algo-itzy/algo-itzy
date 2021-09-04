import sys
from collections import deque


def solve(x, y):
    queue = deque()
    dxdy = [(0, 1),(0, -1),(1, 0),(-1, 0)]

    # 시작점 queue에 넣고 방문 표시, dist도 1 증가
    queue.append((x, y))
    visited[x][y] = 1
    dist[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in dxdy:
            new_x = x + i[0]
            new_y = y + i[1]
            if 0<=new_x<N and 0<=new_y<M and matrix[new_x][new_y] == '1' and not visited[new_x][new_y]:
                # 새로 시작점 append, 방문 표시, dist 업데이트
                queue.append((new_x, new_y))
                visited[new_x][new_y] = 1
                dist[new_x][new_y] = dist[x][y] + 1


input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [input().strip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]  # 방문 여부 표시 리스트
dist = [[0]*M for _ in range(N)]  # 거리 표시 리스트

solve(0,0)
print(dist[N-1][M-1])
