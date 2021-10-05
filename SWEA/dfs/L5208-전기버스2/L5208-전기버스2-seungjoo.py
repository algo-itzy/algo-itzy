# git commit -m "code: Solve swea L5208 전기버스2 (seungjoo)"
for test in range(1, int(input()) + 1):
    N, *battery = map(int, input().split())
    dp = [float('inf')] * N
    dp[N - 1] = 0
    for i in range(N - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if j + battery[j] >= i:
                dp[j] = min(dp[j], dp[i] + 1)
    print(f'#{test} {dp[0] - 1}')