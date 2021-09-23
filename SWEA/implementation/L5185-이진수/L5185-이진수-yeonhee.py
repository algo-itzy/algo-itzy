import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, h = input().split()
    b = bin(int(h, 16))[2:]
    if len(b)%2:
        b = '0' + b
    print(f'#{t} {b}')
