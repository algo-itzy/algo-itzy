import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * (N + 1)
for num in range(1, N + 1):
    dp[num] = dp[num - 1] + nums[num - 1]
for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])