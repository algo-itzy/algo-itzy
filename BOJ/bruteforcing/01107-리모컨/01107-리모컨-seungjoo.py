import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
broken = list(input().split())
init_cnt = abs(N - 100)
for check in range(1000000):
    num = list(str(check))
    for digit in num:
        if digit in broken: 
            break
    else: 
        init_cnt = min(init_cnt, len(str(check)) + abs(check - N))
print(init_cnt)