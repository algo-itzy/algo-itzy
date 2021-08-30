import sys
sys.setrecursionlimit(10 ** 4)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
cnt = 0

def dfs(n):
    visit[n] = 1

    for i in graph[n]:
        if visit[i] == 0:
            dfs(i)
            
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)

# git commit -m "code: Solve boj 11724 연결요소의 개수 (seokzin)"