# git commit -m "code: Solve swea 10966 물놀이를 가자 (seungjoo)"
import sys
sys.stdin = open('input.txt')

for test in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pool = [list(input()) for _ in range(N)]
    dp = [[float('inf')] * M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                dp[i][j] = 0
                continue
            if j:
                dp[i][j] = min(dp[i][j-1] + 1, dp[i][j])
            if i:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j])

    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if pool[i][j] == 'W':
                dp[i][j] = 0
                continue
            if not j == M - 1:
                dp[i][j] = min(dp[i][j+1] + 1, dp[i][j])
            if not i == N - 1:
                dp[i][j] = min(dp[i+1][j] + 1, dp[i][j])
            if dp[i][j] == float('inf'):
                continue
            answer += dp[i][j]

    print(f'#{test} {answer}')