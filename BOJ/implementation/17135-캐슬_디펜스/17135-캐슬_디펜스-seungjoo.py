# git commit -m "code: Solve boj 17135 캐슬 디펜스 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappush


def search_target(x, y):
    if enemies[x][y]: return (x, y)
    q = deque()
    q.append((x, y))
    visited = [[False] * M for __ in range(N)]
    visited[x][y] = True
    target_candidate = []
    for __ in range(D - 1):
        for __ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if enemies[nx][ny]:
                        heappush(target_candidate, (ny, nx))
                    visited[nx][ny] = True
                    q.append((nx, ny))
        if target_candidate:
            y, x = target_candidate[0]
            return (x, y)
    return 0


def start_game(archers):
    deaths = set()
    for row in range(N - 1, -1, -1):
        death = set()
        for archer in archers:
            kill = search_target(row, archer)
            if kill: 
                deaths.add(kill)
                death.add(kill)
        for x, y in death:
            enemies[x][y] = 0
    for x, y in deaths:
        enemies[x][y] = 1
    return len(deaths)


N, M, D = map(int, input().split())
enemies = [list(map(int, input().split())) for __ in range(N)]

archer_combs = []
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            archer_combs.append((i, j, k))

delta = ((0, -1), (-1, 0), (0, 1))
max_kill_cnt = 0
for archer_set in archer_combs:
    max_kill_cnt = max(max_kill_cnt, start_game(archer_set))
print(max_kill_cnt)