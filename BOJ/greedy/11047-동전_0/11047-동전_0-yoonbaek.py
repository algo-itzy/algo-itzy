from sys import stdin

rd = stdin.readline

if __name__ == "__main__":
    N, K = map(int, rd().split())
    coins = [int(rd()) for _ in range(N)]

    cnt = 0
    for i in range(N-1, -1, -1):
        now = coins[i]
        if now > K:
            continue
        cnt += K // now
        K %= now

    print(cnt)
# git commit -m "code: Solve boj 11047 동전 0 (yoonbaek)"