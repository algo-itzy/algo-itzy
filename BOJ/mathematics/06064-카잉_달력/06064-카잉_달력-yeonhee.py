import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    result = -1

    for i in range(x, M*N+1, M):
        if i % N == y % N:
            result = i
            break

    print(result)
