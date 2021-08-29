# 2xn 타일링
#  n cnt methods
#  1   1 1:2*1
#  2   2 1:2*1*2 2:1*2*2
#  3   3 1:2*1*2 2:1*2*2+2*1 3: 2*1+1*2*2
#  4   5
#  5   8

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1

    if n > 1:
        dp[2] = 2

    if n > 2:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n]%10007)

# git commit -m "code: Solve boj 11726 2xn 타일링 (yoonbaek)"