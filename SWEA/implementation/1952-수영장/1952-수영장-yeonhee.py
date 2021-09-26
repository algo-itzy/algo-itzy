import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    daily, monthly, quarterly, yearly = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0]*12

    dp[0] = min(daily * plan[0], monthly)
    dp[1] = dp[0] + min(daily * plan[1], monthly)
    dp[2] = min(dp[1] + min(daily * plan[2], monthly), quarterly)

    for i in range(3, 12):
        dp[i] = min(dp[i-3] + quarterly, dp[i-1] + min(daily * plan[i], monthly))

    dp[-1] = min(dp[-1], yearly)

    print(f'#{t} {dp[-1]}')
