n = int(input())
m = int(input())
arr = input()
dp = [0] * m
res = 0

if arr[0:3] == 'IOI':
    dp[0] = 1

if arr[1:4] == 'IOI':
    dp[1] = 1

for i in range(2, m-2):
    if arr[i:i+3] == 'IOI':
        dp[i] = dp[i-2] + 1

for x in dp:
    if x >= n:
        res += 1

print(res)

# DP에 IOI 카운팅을 메모이제이션해서 어떤 n이 오든 한번에 탐색 가능