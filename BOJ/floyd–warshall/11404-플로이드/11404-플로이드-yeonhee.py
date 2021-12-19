import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
costs = [[100001]*n for _ in range(n)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    costs[s-1][e-1] = min(cost, costs[s-1][e-1])

for k in range(n):
    costs[k][k] = 0
    for i in range(n):
        for j in range(n):
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

for i in range(n):
    for j in range(n):
        if costs[i][j] == 100001:
            costs[i][i] = 0

for row in costs:
    print(*row)
