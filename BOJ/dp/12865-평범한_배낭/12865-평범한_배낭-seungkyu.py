# git commit -m "code: Solve boj 12865 평범한 배낭 (seungkyu)"
import sys
input = sys.stdin.readline
bag = [[0, 0]]
n, k = map(int, input().split())

for _ in range(n):
    w, v = map(int, input().split())
    bag.append([w, v])

# 1차원 dp
dp = [0]*(k+1)
for i in range(1, n+1):
    for j in range(k, 0, -1):
        w = bag[i][0] # i번째 물건의 무게
        v = bag[i][1] # i번째 물건의 가치

        if j-w >= 0:
            # i번째 물건 넣을 수 있는 용량일 때,
            # 용량이 j인 배낭에 i번째 물건 넣었을 때
            dp[j] = max(dp[j], dp[j-w]+v)
print(dp[k])

# 2차원 dp
# dp = [[0]*(k+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         w = bag[i][0] # i번째 물건의 무게
#         v = bag[i][1] # i번째 물건의 가치

#         if j-w < 0:
#             dp[i][j] = dp[i-1][j] # i번째 물건 넣으면 용량 벗어날 때
#         else:
#             # i번째 물건 넣을 수 있는 용량일 때,
#             # 용량이 j인 배낭에 i번째 물건 넣었을 때
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

# print(dp[n][k])