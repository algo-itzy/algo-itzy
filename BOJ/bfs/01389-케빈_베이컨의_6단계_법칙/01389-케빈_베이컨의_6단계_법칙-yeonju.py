# 자기 자신을 제외한 나머지 정점을 탐색하는 데 거치는 수
from collections import deque

def bfs(v):
    cnt = 0
    queue = deque([[v, cnt]])
    while queue:
        value = queue.popleft()
        v = value[0]
        cnt = value[1]
        if not visited[v]:
            visited[v] = True
            cnt_list[v] += cnt
            cnt += 1
            for i in adjacent[v]:
                queue.append([i, cnt])


n, m = map(int, input().split()) # 유저의 수 n, 친구 관계의 수 m
adjacent = [[] for _ in range(n+1)]
cnt_list = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

for i in range(1, n+1):
    visited = [False] * (n+1)
    bfs(i)

print(cnt_list.index(min(cnt_list[1:])))



# git commit -m "code: Solve boj 01389 케빈 베이컨의 6단계 법칙 (yeonju)"