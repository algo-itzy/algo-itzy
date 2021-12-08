# git commit -m "code: Solve boj 01932 정수 삼각형 (seungjoo)"
import sys
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

for row in range(1, N):
    for col in range(row + 1):
        if col == 0:
            triangle[row][col] = triangle[row - 1][col] + triangle[row][col]
        elif col == row:
            triangle[row][col] = triangle[row - 1][row - 1] + triangle[row][col]
        else:
            triangle[row][col] = max(triangle[row - 1][col], triangle[row - 1][col - 1]) + triangle[row][col]

print(max(triangle[N - 1]))