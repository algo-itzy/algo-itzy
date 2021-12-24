# git commit -m "code: Solve boj 12865 평범한 배낭 (seungjoo)"
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
costs = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j < costs[i][0] :
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(costs[i][1] + dp[i - 1][j - costs[i][0]], dp[i - 1][j])

print(dp[N][K])