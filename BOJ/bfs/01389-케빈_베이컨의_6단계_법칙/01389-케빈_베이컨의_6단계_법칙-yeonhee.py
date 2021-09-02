from collections import deque, defaultdict


def bfs(v):
    bacon = [0] * (N+1)
    visited = [0] * (N+1)
    visited[v] = 1
    q = deque([v])

    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                bacon[w] = bacon[v] + 1
                q.append(w)
                visited[w] = 1

    return sum(bacon)


N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []

for i in range(1, N+1):
    result.append(bfs(i))

print(result.index(min(result))+1)
