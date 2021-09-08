# dp문제, 미리 리스트 100개 선언해서 사용했습니다.
def solve(n):
    if n <= 3:
        return dp[n-1]
    else:
        for i in range(3, n):
            dp[i] = dp[i-2] + dp[i-3]
        return dp[n-1]


T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0]*100
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    print(solve(n))

# git commit -m "code: Solve boj 09461 파도반 수열 (seungkyu)"