import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0, 1, 1, 1, 2, 2]

    for i in range(6, N + 1):
        dp.append(dp[i - 1] + dp[i - 5])

    print(dp[N])