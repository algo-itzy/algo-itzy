# bottom-up 방식 dp

N = int(input())
dp = [0 for _ in range(N+1)]

for i in range(2, N+1):
    # 1을 뺄 경우
    dp[i] = dp[i-1] + 1

    # 2로 나누어질 경우, 기존 1을 뺐을 경우의 수와 비교
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    
    # 3으로 나누어질 경우, 앞에서 구한 최솟값과 비교
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])

