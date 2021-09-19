N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for r in range(N):
        for c in range(N):
            if graph[r][k] and graph[k][c]:
                graph[r][c] = 1

for row in graph:
    for col in row:
        print(col, end=" ")
    print()
