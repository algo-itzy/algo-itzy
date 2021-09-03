n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * n

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[1] + arr[2], arr[0]+arr[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

    print(dp[n-1])

# 어떻게 이 DP만으로 계단 규칙을 장담할 수 있을까
# 예외처리를 없애기가 어렵다..