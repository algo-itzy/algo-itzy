# git commit -m "code: Solve boj 09251 LCS (seungjoo)"
import sys
input = sys.stdin.readline

a, b = input().strip(), input().strip()
n, m = len(a), len(b)
dp = [[0] * (m + 1) for _ in range(n + 1)] 

for i in range(n): 
    for j in range(m): 
        dp[i + 1][j + 1] = dp[i][j] + 1 if a[i] == b[j] else max(dp[i + 1][j], dp[i][j + 1]) 

print(dp[-1][-1])