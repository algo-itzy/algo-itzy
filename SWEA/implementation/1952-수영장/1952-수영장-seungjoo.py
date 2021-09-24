# git commit -m "code: Solve swea 1952 수영장 (seungjoo)"
for test in range(1, int(input()) + 1):
    # 0, 1, 2, 3: 1일, 1달, 3개월, 1년
    costs = list(map(int, input().split()))
    annual_plans = [0] + list(map(int, input().split()))

    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = dp[i-1] + min(costs[0] * annual_plans[i], costs[1])
        if i > 2:
            dp[i] = min(dp[i], dp[i-3] + costs[2])
    answer = min(dp[12], costs[3])
    print(f'#{test} {answer}')
