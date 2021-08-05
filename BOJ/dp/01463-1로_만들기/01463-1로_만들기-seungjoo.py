import sys
input=sys.stdin.readline

N=int(input())
dp = [0 for _ in range(N+1)]

# index i를 N으로 활용하기 위해 자연수로 맞춰준다.
# 일단 1칸 움직이는 선택지는 다른 선택지에 비해 무조건 큰 값을 가지니 선행한다.
# 추후 조건이 맞으면 이전 수행횟수에서 1을 더한값과 비교해 저장한다.
for i in range(2,N+1):
    dp[i] = dp[i-1]+1
    if not i%2:
        dp[i] = min(dp[i],dp[i//2]+1)
    if not i%3:
        dp[i] = min(dp[i],dp[i//3]+1)
print(dp[N])