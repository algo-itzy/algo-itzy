import sys
input = sys.stdin.readline


# 플로이드 워셜 탐색
N, M = map(int, input().split())
graph = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,N+1):
    graph[k][k] = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

min_sum_user = float('inf')
for i in range(1,N+1):
    sum_friends = 0
    for j in range(N+1):
        if graph[i][j] != float('inf'):
            sum_friends += graph[i][j]
    if min_sum_user > sum_friends:
        min_sum_user = sum_friends
        answer = i

print(answer)