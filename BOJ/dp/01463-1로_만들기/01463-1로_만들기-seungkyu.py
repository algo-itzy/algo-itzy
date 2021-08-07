def solve(num, dp):
    # num값까지의 값을 구하기 위해 그 전의 정답값들을 모두 도출
    for i in range(2, num+1):
        dp[i] = dp[i-1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        # 2로 나누는 테스트는 3으로 나누는 것과 따로 검증해야 하므로 elif 사용하면 안됨
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
    print(dp[num])

if __name__ == "__main__":
    num = int(input())
    dp = [0] * (num+1) # ex) dp[4] => 인풋이 숫자 4일때의 정답값
    solve(num, dp)
