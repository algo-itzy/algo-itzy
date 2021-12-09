n = int(input())

rgb = []
dp = [[0]*3 for _ in range(n+1)]

for _ in range(n):
    cost = list(map(int, input().split()))
    rgb.append(cost)

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i-1][2]

print(min(dp[n]))

# 가독성을 위해 dp와 rgb를 개별 분리했음