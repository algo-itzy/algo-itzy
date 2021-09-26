# git commit -m "code: Solve swea 1953 탈주범 검거 (seungjoo)"
import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(x, y, cur_type, time):
    q = deque()
    q.append((x, y, cur_type, time))
    visited[x][y] = True
    answer = 1
    while q:
        x, y, cur_type, time = q.popleft()
        for direction in tunnels[cur_type]:
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] and not visited[nx][ny] and time < L:
                if direction == 0 or direction == 1:
                    if direction ^ 1 in tunnels[matrix[nx][ny]]:
                        visited[nx][ny] = True
                        q.append((nx, ny, matrix[nx][ny], time + 1))
                        answer += 1
                else:
                    if (direction+1) % 2 + 2 in tunnels[matrix[nx][ny]]:
                        visited[nx][ny] = True
                        q.append((nx, ny, matrix[nx][ny], time + 1))
                        answer += 1
    return answer


for test in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    tunnels = {1: [0, 1, 2, 3], 2: [2, 3], 3: [0, 1], 4: [2, 0], 5: [0, 3], 6: [1, 3], 7: [1, 2]}
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    print(f'#{test} {bfs(R, C, matrix[R][C], 1)}')