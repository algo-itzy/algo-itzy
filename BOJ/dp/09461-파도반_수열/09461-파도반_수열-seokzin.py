dp = [0, 1, 1, 1, 2, 2]

for i in range(5, 100):
    dp.append(dp[i] + dp[i-4])

for _ in range(int(input())):
    print(dp[int(input())])

# 점화식이 2개가 나오는데 먼저 떠오른 걸로 씁니다.