# git commit -m "code: Solve boj 12865 평범한 배낭 (jiwoong)"
import sys

N, K = map(int, sys.stdin.readline().split())

bag = [[0, 0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    bag.append([W, V])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = bag[i][0]
        v = bag[i][1]

        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])

print(dp[N][K])
