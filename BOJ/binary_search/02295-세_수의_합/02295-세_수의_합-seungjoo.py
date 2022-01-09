# git commit -m "code: Solve boj 02295 세 수의 합 (seungjoo)"
import sys
input = sys.stdin.readline

N = int(input())
U = [int(input()) for _ in range(N)]
U.sort()
ab_arr = set()
for i in range(N):
    for j in range(N):
        ab_arr.add(U[i] + U[j])

for i in range(N - 1, 0, -1):
    for j in range(i):
        if U[i] - U[j] in ab_arr:
            print(U[i])
            exit()