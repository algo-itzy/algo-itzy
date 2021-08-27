import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))

P.sort()
answer = 0
for i in range(N):
    answer += (N-i)*P[i]
print(answer)