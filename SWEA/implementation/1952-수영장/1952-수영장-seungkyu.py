# git commit -m "code: Solve swea 1952 수영장 (seungkyu)"
T = int(input())
for tc in range(1, T+1):

    price_d, price_m, price_t, price_y = map(int, input().split())
    nums = [0] + list(map(int, input().split()))
    dp = [0]*13
    dp[1] = min(nums[1]*price_d, price_m)
    dp[2] = min(dp[1]+nums[2]*price_d, dp[1]+price_m, price_t)
    dp[3] = min(dp[2]+nums[3]*price_d, dp[2]+price_m, price_t)
    for i in range(4, 13):
        dp[i] = min(dp[i-1]+nums[i]*price_d, dp[i-1]+price_m, dp[i-3]+price_t)

    print(f'#{tc} {min(dp[12], price_y)}')
