# git commit -m "code: Solve boj 11053 가장 긴 증가하는 부분 수열 (jiwoong)"
import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

seq = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            seq[i] = max(seq[i], seq[j] + 1)

print(max(seq))
