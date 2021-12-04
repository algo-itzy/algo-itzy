import sys
from collections import deque

input = sys.stdin.readline


def bfs(n):
    global max_dis
    global max_index

    visit = [0] * (v+1)
    dis = [0] * (v+1)

    q = deque(([n]))
    visit[n] = 1

    while q:
        t = q.popleft()

        for i, d in graph[t]:
            if not visit[i]:
                visit[i] = 1
                dis[i] = dis[t] + d
                q.append(i)

                if max_dis < dis[i]:
                    max_dis = dis[i]
                    max_index = i


v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    path = list(map(int, input().split()))

    for i in range(1, len(path)-2, 2):
        graph[path[0]].append((path[i], path[i+1]))

max_dis = 0
max_index = 0

bfs(1)
bfs(max_index) # 여기서 지름 거리 구해짐

print(max_dis)

# 노드 x에서 가장 거리가 먼 노드가 지름 중 한쪽이 됨. 거기서 최장거리 노드를 뽑으면 지름.