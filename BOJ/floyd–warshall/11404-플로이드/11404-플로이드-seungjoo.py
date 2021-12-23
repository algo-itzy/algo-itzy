# git commit -m "code: Solve boj 11404 플로이드 (seungjoo)"
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
bus_datas = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus_datas[a - 1][b - 1] = min(bus_datas[a - 1][b - 1], c)

for k in range(n):
    bus_datas[k][k] = 0
    for i in range(n):
        for j in range(n):
            if bus_datas[i][j] > bus_datas[i][k] + bus_datas[k][j]:
                bus_datas[i][j] = bus_datas[i][k] + bus_datas[k][j]

for i in range(n):
    for j in range(n):
        if bus_datas[i][j] == float('inf'):
            bus_datas[i][j] = 0

for row in bus_datas:
    print(*row)
