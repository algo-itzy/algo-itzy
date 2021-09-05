n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n == 1:
    print(stairs[1])

elif n == 2:
    print(stairs[1] + stairs[2])

else:
    dp[1] = stairs[1]
    dp[2] = stairs[2] + stairs[1]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i] + stairs[i-1])

    print(dp[n])
