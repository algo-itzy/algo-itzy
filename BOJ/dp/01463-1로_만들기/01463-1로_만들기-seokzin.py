n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = min(dp[i//2 if i%2==0 else i-1]+1, dp[i//3 if i%3==0 else i-1]+1)
        
print(dp[n])

# 3으로 나누는게 항상 최적을 보장하지 않는다. -> DP를 써야한다.
# d(n) = min(d(n//3), d(n//2), d(n-1)) + 1
# if 분기 없이 풀려고 쇼를 했습니다. 가독성 쏘리..😅