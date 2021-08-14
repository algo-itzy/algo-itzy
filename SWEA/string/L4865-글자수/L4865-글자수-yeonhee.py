import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1):
    str1, str2 = input(), input()
    result = 0

    for char in str1:
        result = max(result, str2.count(char))

    print(f'#{t} {result}')
