# git commit -m "code: Solve boj 01932 정수 삼각형 (jiwoong)"
import sys

input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    num = len(tri[i])
    for j in range(num):
        if j == 0:
            tri[i][j] += tri[i - 1][j]
        elif j == num - 1:
            tri[i][j] += tri[i - 1][j - 1]
        else:
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])
print(max(tri[n - 1]))
