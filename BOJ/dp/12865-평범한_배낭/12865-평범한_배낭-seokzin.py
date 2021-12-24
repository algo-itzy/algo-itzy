n, k = map(int, input().split())
bag = []
dp = [0 for _ in range(k+1)]

for _ in range(n):
    w, v = map(int, input().split())
    bag.append([w, v])

for i in range(n):
    i_w, i_v = bag[i][0], bag[i][1]

    for j in range(k, 0, -1):
        if j >= i_w:
            dp[j] = max(dp[j], dp[j-i_w]+i_v)

print(dp[-1])