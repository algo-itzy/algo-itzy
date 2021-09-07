import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
ans = 0
for i in range(N - 1, -1, -1):
    if K == 0:
        break
    if K >= A[i]:
        ans = ans + K // A[i]
        K = K % A[i]
print(ans)
