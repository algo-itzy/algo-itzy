import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    for next in nodes[start]:
        if not visited[next]:
            dfs(next)
            
N, M = map(int, input().split())
nodes = {i:[] for i in range(1, N+1)}
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

cnt = 0  # 답
for i in range(1, N+1):  # 1부터 돌면서 연결 요소 찾기
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
