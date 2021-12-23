# git commit -m "code: Solve boj 11404 플로이드 (seungkyu)"
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print(0, end=' ')
        else:
            if dist[i][j] == float('inf'):
                dist[i][j] = 0
            print(dist[i][j], end=' ')
    print()