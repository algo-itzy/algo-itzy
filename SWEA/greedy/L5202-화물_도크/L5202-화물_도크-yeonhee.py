import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    data = [tuple(map(int, input().split())) for _ in range(int(input()))]
    data.sort(key=lambda x: (x[1], x[0]))
    result = 0
    last = 0

    for s, e in data:
        if s >= last:
            result += 1
            last = e

    print(f'#{t} {result}')
