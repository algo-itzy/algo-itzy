import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m  = map(int, input().split())
graph = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1  # 비용은 1로 넣는다.
    graph[b-1][a-1] = 1

for k in range(n): # 경유지
    for i in range(n):
        for j in range(n):
            if i == j: # 출발-도착 같으면 0으로 초기화
                graph[i][j] = 0 
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# INF를 0으로 변환
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

costs = list(map(sum, graph))  # row별 cost를 리스트에 모은다
print(costs.index(min(costs)) + 1)

# 연습하고 싶어서 일부로 플로이드 워셜로 풀었습니다.