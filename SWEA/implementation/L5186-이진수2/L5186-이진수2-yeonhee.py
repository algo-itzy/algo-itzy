import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = float(input())
    result = ''

    for i in range(-1, -14, -1):
        result += str(int(n // 2**i))
        n %= 2**i
        if n == 0:
            break
    else:
        result = 'overflow'

    print(f'#{t} {result}')
