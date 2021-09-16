n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

for row in graph:
    print(*row)

# DFS가 더 간단하지만 플로이드-워셜을 flag 처럼 사용하여 풀이