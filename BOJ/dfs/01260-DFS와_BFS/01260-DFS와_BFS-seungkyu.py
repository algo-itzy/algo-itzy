import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

stack = []  # dfs stack
ans1 = []
def dfs(nodes, start):
    visited[start] = 1
    ans1.append(start)
    stack.extend(sorted(nodes[start], reverse=True))  # 작은 노드부터 돌도록
    while stack:
        next = stack.pop()
        if not visited[next]:  # 방문하지 않은 노드만 방문
            dfs(nodes, next)

queue = deque()  # bfs queue
ans2 = []
def bfs(nodes, start):
    queue.extend(sorted(nodes[start]))  # 작은 노드부터 돌도록
    visited[start] = 1
    ans2.append(start)
    while queue:
        next = queue.popleft()
        if not visited[next]:  # 방문하지 않은 노드만 방문
            visited[next] = 1
            queue.extend(sorted(nodes[next]))
            ans2.append(next)
        
N, M, V = map(int, input().split())
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [0]*(N+1)
dfs(nodes, V)
visited = [0]*(N+1)  # visited reset
bfs(nodes, V)

print(*ans1)
print(*ans2)
