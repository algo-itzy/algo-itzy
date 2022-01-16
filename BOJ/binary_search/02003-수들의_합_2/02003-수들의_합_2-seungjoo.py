# git commit -m "code: Solve boj 02003 수들의 합 2 (seungjoo)"
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
left, tmp, cnt = 0, 0, 0
for right in range(N):
    tmp += arr[right]
    while tmp > M:
        tmp -= arr[left]
        left += 1
    if tmp == M:
        cnt += 1
print(cnt)
