import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(n)]

dp = [[0] * (n+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, n+1):
        dp[x][y] = board[x-1][y-1] + dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(ans)


# git commit -m "code: Solve boj 11660 구간 합 구하기 5 (yeonju)"