import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    chars = input()
    stack = []

    for char in chars:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{t} {len(stack)}')
