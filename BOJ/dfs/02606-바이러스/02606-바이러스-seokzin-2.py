from collections import deque

def bfs(n):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if not visit[x]:
            visit[x] = 1

            for nx in graph[x]:
                q.append(nx)

n = int(input())
k = int(input())

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

print(sum(visit)-1)  # 1번 컴퓨터 제외