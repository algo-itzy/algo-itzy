import sys
input = sys.stdin.readline
# A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수) 라는 조건에 맞춘 풀이
N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

cnt = 0
for coin in coins[::-1]:  # 큰 코인부터 살펴봄(코인 개수 최소)
    if K // coin >= 1:  # 1개 이상 사용 가능할 때 진행
        cnt += K // coin
        K = K - (K // coin)*coin

print(cnt)

# git commit -m "code: Solve boj 11047 동전 0 (seungkyu)"