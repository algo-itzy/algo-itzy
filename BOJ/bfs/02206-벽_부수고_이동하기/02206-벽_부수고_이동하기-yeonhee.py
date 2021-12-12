import sys
from collections import deque

input = sys.stdin.readline
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs():
    q = deque([(0, 0, 1)])
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1

    while q:
        r, c, w = q.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c][w]

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 1 and w == 1:
                    q.append((nr, nc, 0))
                    visited[nr][nc][0] = visited[r][c][1] + 1

                elif board[nr][nc] == 0 and visited[nr][nc][w] == 0:
                    q.append((nr, nc, w))
                    visited[nr][nc][w] = visited[r][c][w] + 1

    return -1


N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
print(bfs())
