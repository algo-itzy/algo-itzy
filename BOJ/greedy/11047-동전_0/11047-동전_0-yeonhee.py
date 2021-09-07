import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)][::-1]

result = 0

for coin in coins:
    if not K:
        break

    result += K//coin
    K %= coin

print(result)
