for tc in range(1, int(input())+1):
    a, b, c, d = map(int, input().split())  # 1일, 1달, 3달, 1년
    arr = [0] + list(map(int, input().split()))
    dp = [0] * 13

    dp[1] = min(a*arr[1], b)
    dp[2] = dp[1] + min(a*arr[2], b)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + c, dp[i-1] + b, dp[i-1] + arr[i]*a)

    print(f"#{tc}", min(dp[-1], d))
