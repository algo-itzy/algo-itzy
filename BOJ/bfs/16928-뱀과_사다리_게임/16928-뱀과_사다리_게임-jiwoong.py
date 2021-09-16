import sys
from collections import deque

input = sys.stdin.readline
board = 100


def bfs(lad, visit):
    q = deque([1])
    visit[1] = 0
    while q:
        v = q.popleft()
        if visit[v] >= visit[100]:
            continue
        for dice in range(1, 7):
            if v + dice > 100:
                continue
            num = lad[v + dice]
            if visit[num] >= board:
                q.append(num)
                visit[num] = visit[v] + 1
    return visit[100]


n, m = map(int, input().split())
lad = list(range(101))
for _ in range(n + m):
    x, y = map(int, input().split())
    lad[x] = y
visit = [board] * 101
print(bfs(lad, visit))
