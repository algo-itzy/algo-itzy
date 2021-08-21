import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(m):
        numbers.append(numbers.pop(0))
    print(f'#{t} {numbers[0]}')
