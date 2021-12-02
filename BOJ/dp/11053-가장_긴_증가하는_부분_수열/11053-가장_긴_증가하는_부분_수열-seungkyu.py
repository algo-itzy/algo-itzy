# git commit -m "code: Solve boj 11053 가장 긴 증가하는 부분 수열 (seungkyu)"
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

ans = 0
dp = [1]*n

ans = 1
for i in range(1, n):
    cnt = 1
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)
    ans = max(ans, dp[i])

print(ans)