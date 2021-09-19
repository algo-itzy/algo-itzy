N = int(input())
dp = [0] * 50001
dp[1] = 1

for i in range(1, N + 1):
    cnt = 0
    tmp = i
    while tmp:
        a = int(tmp**0.5) ** 2
        tmp -= a
        cnt += 1
    dp[i] = cnt

    for j in range(1, int(i**0.5) + 1):
        dp[i] = min(dp[i], dp[j*j] + dp[i - j*j])

print(dp[N])
