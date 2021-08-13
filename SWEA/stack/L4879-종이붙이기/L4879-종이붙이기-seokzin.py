T = int(input())

for tc in range(1, T+1):
    N = int(input())

    dp = [1, 3]

    for i in range(2, N//10):
        dp.append(dp[i-1] + 2*dp[i-2])

    print(f"#{tc} {dp[-1]}")

# 규칙을 찾아 점화식을 구현하는 문제