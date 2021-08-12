import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    str1 = input()
    str2 = input()

    print(f'#{t}', end=' ')
    print(1 if str1 in str2 else 0)
