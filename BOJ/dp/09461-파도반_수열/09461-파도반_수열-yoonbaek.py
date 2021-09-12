from sys import stdin

rd = lambda: int(stdin.readline())

if __name__ == "__main__":
    dp = [0] * (100)
    dp[0], dp[1], dp[2] = 1, 1, 1

    for i in range(3, 100):
        dp[i] = dp[i-2] + dp[i-3]

    for _ in range(rd()):
        print(dp[rd()-1])
# git commit -m "code: Solve boj 09461 파도반 수열 (yoonbaek)"