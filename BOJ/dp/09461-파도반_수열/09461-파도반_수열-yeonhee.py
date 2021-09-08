dp = [0, 1, 1, 1]

for i in range(4, 101):
    dp += [dp[i-3] + dp[i-2]]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
