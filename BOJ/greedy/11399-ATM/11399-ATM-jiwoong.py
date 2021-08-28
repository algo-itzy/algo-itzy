import sys
input = sys.stdin.readline

N = int(input())
wait = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += wait[i] * (N - i)
print(ans)