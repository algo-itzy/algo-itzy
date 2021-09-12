import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
presum = [0] * (n+1)  # 부분합

for i in range(n):
    presum[i+1] = presum[i] + arr[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(presum[b] - presum[a-1])