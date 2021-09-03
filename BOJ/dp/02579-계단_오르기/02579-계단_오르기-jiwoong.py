import sys

input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]
num.reverse()

dp = [0] * N
dp[0] = num[0]

for i in range(1, N):
    if i < 3:
        dp[i] = num[0] + num[i]
    else:
        dp[i] = max(dp[i - 2] + num[i], dp[i - 3] + num[i - 1] + num[i])

print(max(dp[N - 2], dp[N - 1]))
