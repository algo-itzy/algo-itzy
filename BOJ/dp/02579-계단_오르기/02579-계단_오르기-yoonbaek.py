from sys import stdin

if __name__ == "__main__":
    stairs = list(map(int, stdin.read().split("\n")[:-1]))
    N = stairs[0]
    stairs = stairs[1:]

    dp = [0] * N

    for n in range(0, N):
        if n == 0:
            dp[n] = stairs[0]
        elif n == 1:
            dp[n] = max(stairs[0], stairs[0] + stairs[1])
        elif n == 2:
            dp[n] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
        else:
            dp[n] = max(dp[n-3] + stairs[n-1] + stairs[n], dp[n-2] + stairs[n])
    
    print(dp[N-1])
# git commit -m "code: Solve boj 02579 계단 오르기 (yoonbaek)"