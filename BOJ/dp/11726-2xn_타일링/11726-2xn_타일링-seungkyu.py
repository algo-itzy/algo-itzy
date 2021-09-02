import sys
input = sys.stdin.readline
# 시간 초과 안나도록 조심
dp = [0, 1, 2]
for i in range(3, 1001):
    dp.append(dp[i-1] + dp[i-2])

n = int(input())
print(dp[n]%10007)
