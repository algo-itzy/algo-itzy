import sys
from collections import deque

input= sys.stdin.readline

n,m = map(int, input().split())       # 정점의 개수 n, 간선의 개수 m
graph = [[]*n for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)          # 노드 들의 정보를 graph 리스트에 저장
    graph[b].append(a)

visited = [0] * (n+1)           # 노드 방문 체크를 위한 리스트 0으로 초기

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] ==0:
                queue.append(i)
                visited[i] = 1

cnt = 0
for i in range(1, n+1):
    if visited[i]==0:
        bfs(i)
        cnt+=1

print(cnt)



# git commit -m "code: Solve boj 11724 연결요소의 개수 (yeonju)"