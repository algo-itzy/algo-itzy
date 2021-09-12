# git commit -m "code: Solve boj 09461 파도반 수열 (seungjoo)"
for _ in range(int(input())):
    n = int(input())
    dp = [1,1,1,2,2]
    if n>5:
        for i in range(5,n):
            dp.append(dp[i-1]+dp[i-5])
    print(dp[n-1])