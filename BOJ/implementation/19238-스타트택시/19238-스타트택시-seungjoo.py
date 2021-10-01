# git commit -m "code: Solve boj 19238 스타트택시 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappush


def go_target(start_x, start_y, start_oil):
    q = deque()
    q.append((start_x, start_y, start_oil))
    visited = [[False] * N for __ in range(N)]
    visited[start_x][start_y] = True
    while q:
        for __ in range(len(q)):
            x, y, rest = q.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not maps[nx][ny] and not visited[nx][ny] and rest:
                    if (nx, ny) == passengers[(start_x, start_y)]:
                        del passengers[(start_x, start_y)]
                        rest -= 1
                        new_oil = rest + 2 * (start_oil - rest)
                        return (nx, ny), new_oil
                    visited[nx][ny] = True
                    q.append((nx, ny, rest - 1))
    return 0, rest


def take_passenger(start_oil):
    q = deque()
    x, y = taxi
    if taxi in passengers:
        return go_target(x, y, start_oil)
    q.append((x, y, start_oil))
    visited = [[False] * N for __ in range(N)]
    visited[x][y] = True
    sets = []
    while q:
        for __ in range(len(q)):
            x, y, rest = q.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not maps[nx][ny] and not visited[nx][ny] and rest:
                    if (nx, ny) in passengers:
                        heappush(sets, (nx, ny, rest - 1))
                    visited[nx][ny] = True
                    q.append((nx, ny, rest - 1))
        if sets:
            start_x, start_y, rest_oil = sets[0]
            return go_target(start_x, start_y, rest_oil)
    return 0, rest
            
            
N, M, oil = map(int, input().split())
maps = [list(map(int, input().split())) for __ in range(N)]
taxi = tuple(map(lambda x: int(x)-1, input().split()))
passengers = {}
for _ in range(M):
    a, b, c, d = map(int, input().split())
    if (a, b) == (c, d):
        continue
    passengers[(a-1, b-1)] = (c-1, d-1)

delta = ((0, -1), (0, 1), (1, 0), (-1, 0))

while len(passengers):
    if not taxi or not oil:
        print(-1)
        break
    taxi, oil = take_passenger(oil)
else:
    print(oil)