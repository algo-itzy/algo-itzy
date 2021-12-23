n, k = map(int ,input().split()) # 물품의 수 n, 버틸 수 있는 무게 k

dp = [[0]*(k+1) for _ in range(n+1)]
index = []
value = []

for i in range(n):
    w, v = map(int, input().split())
    index.append(w)
    value.append(v)


for i in range(n+1):
    for j in range(k+1):
        if index[i-1] <= j:
            dp[i][j] = max(value[i-1] + dp[i-1][j-index[i-1]] , dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])


# git commit -m "code: Solve boj 12865 평범한 배낭 (yeonju)"