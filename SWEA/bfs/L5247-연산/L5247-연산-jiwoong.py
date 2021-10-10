# git commit -m "code: Solve swea L5247 연산 (jiwoong)"
from collections import deque


# 최소 -> 큐
def bfs(i):  # 연산 전 숫자
    global ans
    q = deque()
    q.append(i)
    visited = [0] * 1000001
    while q:
        i = q.popleft()
        if i == M:
            ans = visited[i]
            return
        for v in (i + 1, i - 1, i * 2, i - 10):
            if 0 <= v <= 1000000 and not visited[v]:
                visited[v] = visited[i] + 1
                q.append(v)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = 0
    bfs(N)
    print("#{} {}".format(tc, ans))
