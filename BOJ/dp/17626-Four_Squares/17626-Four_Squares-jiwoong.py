n = int(input())

dp = [0] * 50001
dp[1] = 1

for x in range(1, n + 1):
    ans = 0
    i = x
    while i:
        a = int(i ** 0.5) ** 2
        i -= a
        ans += 1
    dp[x] = ans

    for j in range(1, int(x ** 0.5) + 1):
        dp[x] = min(dp[x], dp[j * j] + dp[x - j * j])

print(dp[n])
