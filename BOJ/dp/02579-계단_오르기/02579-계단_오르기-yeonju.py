# 한번 움직일 때 1 or 2 칸
# 연속된 3개 x
# 마지막 도착 계단은 꼭 밟기

n = int(input()) 

stairs=[0]
for i in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[1])
else:
    dp = [0] * (n+1)
    dp[1] = stairs[1]
    dp[2] = stairs[1]+ stairs[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    
    print(dp[n])

# git commit -m "code: Solve boj 02579 계단 오르기 (yeonju)"