import sys
from collections import deque
sys.stdin = open('input.txt')


def check(nr, nc):
    return 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and (not maze[nr][nc] or maze[nr][nc] == 3)


def bfs(sr, sc):
    queue = deque([(sr, sc)])
    result = 0

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if check(nr, nc):
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                if maze[nr][nc] == 3:
                    result = visited[nr][nc] - 1
                    return result

    return result


for t in range(1, int(input())+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[0] * n for _ in range(n)]

    # 시작 인덱스 찾기
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                sr, sc = r, c

    print(f'#{t} {bfs(sr, sc)}')
