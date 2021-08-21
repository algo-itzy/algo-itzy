import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    opcode = list(input().split())
    stack = []

    try:
        for op in opcode:
            if op.isdigit():
                stack.append(int(op))
            elif op == '.':
                result = stack.pop()
                if stack:
                    result = 'error'
            else:
                num2, num1 = stack.pop(), stack.pop()
                if op == '+': res = num1 + num2
                elif op == '*': res = num1 * num2
                elif op == '-': res = num1 - num2
                elif op == '/': res = num1 // num2
                stack.append(res)

    except:
        result = 'error'

    print(f'#{t} {result}')

"""
if 한줄코딩을 별로 좋아하지는 않지만,
가독성을 위해 이렇게 했습니다. 
"""
