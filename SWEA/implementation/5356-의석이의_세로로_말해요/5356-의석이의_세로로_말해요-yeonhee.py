import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    strings = [input() for _ in range(5)]
    vertical = ''

    for c in range(15):
        for r in range(5):
            if len(strings[r]) > c:
                vertical += strings[r][c]

    print(f'#{t} {vertical}')
