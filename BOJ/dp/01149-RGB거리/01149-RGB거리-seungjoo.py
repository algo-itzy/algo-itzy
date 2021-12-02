# git commit -m "code: Solve boj 01149 RGB거리 (seungjoo)"
import sys
input = sys.stdin.readline

N = int(input())
c = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,N):
    c[i][0] = min(c[i-1][1], c[i-1][2]) + c[i][0]
    c[i][1] = min(c[i-1][0], c[i-1][2]) + c[i][1]
    c[i][2] = min(c[i-1][0], c[i-1][1]) + c[i][2]

print(min(c[N-1][0], c[N-1][1], c[N-1][2]))