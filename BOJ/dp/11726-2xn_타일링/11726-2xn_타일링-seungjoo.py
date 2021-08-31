import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(n+1)

dp[0] = 0
dp[1] = 1
if n>=2:
    dp[2] = 2
if n>=3:
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)