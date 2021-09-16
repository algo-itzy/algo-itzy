import sys
input = sys.stdin.readline

def dfs(v):
    for i in range(n):
        if res[i] == 0 and graph[v][i] == 1: # 연결된 정점을 res 에 방문처리 
            res[i] = 1
            dfs(i)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

res = [0 for _ in range(n)]

for i in range(n):
    dfs(i)
    print(*res)

    res = [0 for _ in range(n)]


# git commit -m "code: Solve boj 11403 경로 찾기 (yeonju)"