n = int(input())

costs = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
    costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]

print(min(costs[n-1][0], costs[n-1][1], costs[n-1][2]))


# git commit -m "code: Solve boj 01149 RGB거리 (yeonju)"