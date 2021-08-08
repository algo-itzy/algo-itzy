def dfs(n):
    if not visit[n]:
        visit[n] = 1

        for nx in graph[n]:
            dfs(nx)

n = int(input())
k = int(input())

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

print(sum(visit)-1)  # 1번 컴퓨터 제외