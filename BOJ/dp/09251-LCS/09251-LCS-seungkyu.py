# git commit -m "code: Solve boj 09251 LCS (seungkyu)"
import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            dp[i+1][j+1] += dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            
print(dp[len(b)][len(a)])