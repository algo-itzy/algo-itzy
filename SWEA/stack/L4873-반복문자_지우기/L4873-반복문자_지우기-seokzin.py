T = int(input())

for tc in range(1, T+1):
    s = input()
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    print(f'#{tc}', len(stack))