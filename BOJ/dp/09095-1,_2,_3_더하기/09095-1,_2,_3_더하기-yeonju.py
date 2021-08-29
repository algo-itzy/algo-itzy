t = int(input())

dp = [0] * 11 # n은 양수, 11 미만 

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11): 
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] 

for tc in range(t):
    n = int(input()) 
    print(dp[n])


# git commit -m "Solve boj 09095 1, 2, 3 더하기 (yeonju)"