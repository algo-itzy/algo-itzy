# git commit -m "code: Solve boj 11047 동전 0 (seungjoo)"
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _  in range(N)]
cnt = 0
for i in range(1,N+1):
    cnt += K // coins[-i]
    K = K % coins[-i]
print(cnt)