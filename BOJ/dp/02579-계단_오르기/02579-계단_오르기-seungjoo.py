import sys
input = sys.stdin.readline

n = int(input())
score =[0] + [int(input()) for _ in range(n)]
dp=[0,score[1]]
if n >= 2:
    dp.append(score[1]+score[2])
if n >= 3:
    for i in range(3,n+1): 
        dp.append(max(dp[i-2]+score[i],dp[i-3]+score[i]+score[i-1]))

print(dp[n])