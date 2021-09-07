from math import gcd

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    for i in range(int(N / gcd(M, N))):
        ans = x + M * i
        if ans % N == y % N:
            break
        else:
            ans = -1
    print(ans)
