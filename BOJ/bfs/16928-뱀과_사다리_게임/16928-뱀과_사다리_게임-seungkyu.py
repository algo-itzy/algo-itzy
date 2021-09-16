# git commit -m "code: Solve boj 16928 뱀과 사다리 게임 (seungkyu)"
import sys
from collections import deque
input = sys.stdin.readline

DIRS = (1, 2, 3, 4, 5, 6)

def bfs():
    q = deque([1])
    end = 100

    while q:
        cur = q.popleft()

        if cur == end:
            return dist[end]

        for i in DIRS:
            pos = cur + i
            if pos in ladders_snakes:
                pos = ladders_snakes[pos]
            if pos <= end and not dist[pos]:
                dist[pos] = dist[cur] + 1    
                q.append(pos)


N, M = map(int, input().split())
ladders_snakes = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders_snakes[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    ladders_snakes[u] = v

dist = [0]*(101)
print(bfs())
