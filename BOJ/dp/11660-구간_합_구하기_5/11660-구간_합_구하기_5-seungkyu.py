# git commit -m "code: Solve boj 11660 구간 합 구하기 5 (seungkyu)"
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sums = [[0]*(n+1) for _ in range(n+1)]
answer = []

for i in range(1, n+1):
    for j in range(1, n+1):
        sums[i][j] = board[i-1][j-1] + sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        answer.append(board[x1-1][y1-1])
    else:
        ans = sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1]
        answer.append(ans)

print(*answer, sep='\n')