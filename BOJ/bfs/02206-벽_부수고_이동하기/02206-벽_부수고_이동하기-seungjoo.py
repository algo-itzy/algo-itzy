# git commit -m "code: Solve boj 02206 벽 부수고 이동하기 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append([0, 0, 1])
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        x, y, key = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][key]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이있고 뚫을 능력이 있을때.
                if maze[nx][ny] == 1 and key == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])
                # 벽이 없고 가보지 않은 곳.
                elif maze[nx][ny] == 0 and visited[nx][ny][key] == 0:
                    visited[nx][ny][key] = visited[x][y][key] + 1
                    q.append([nx, ny, key])
    return -1


n, m = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(n)]

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

print(bfs())