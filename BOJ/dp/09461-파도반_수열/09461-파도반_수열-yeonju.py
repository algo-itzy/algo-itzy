t = int(input())

for tc in range(t):
    n = int(input())

    dp = [1, 1, 1, 2, 2]

    if n>5:
        for i in range(5,n):
            dp.append(dp[i-5] + dp[i-1])

    print(dp[n-1])


# git commit -m "code: Solve boj 09461 파도반 수열 (yeonju)"