import sys
input = sys.stdin.readline

for _ in range(int(input())):
    H, W, N = map(int, input().split())
    if N % H == 0:
        floor, unit = H, N//H
    else:
        floor, unit = N % H, N//H + 1
    print (floor * 100 + unit)
