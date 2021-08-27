import sys
input = sys.stdin.readline


dp = [0 for _ in range(11)]
for i in range(4,11):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
for _ in range(int(input())):
    N = int(input())

    print(dp[N])