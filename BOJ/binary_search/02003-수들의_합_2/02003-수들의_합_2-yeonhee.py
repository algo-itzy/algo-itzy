import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

right, tmp, result = 0, 0, 0

for i in range(N):
    while tmp < M and right < N:
        tmp += nums[right]
        right += 1
    if tmp == M:
        result += 1
    tmp -= nums[i]

print(result)
