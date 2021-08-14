import sys
sys.stdin = open('input.txt')


def solution(sentence):
    stack = []

    for char in sentence:
        if char in ('(', '{'):
            stack.append(char)
        elif char in (')', '}'):
            # 여는 괄호가 없는데 닫는 괄호가 온 경우
            if not stack:
                return 0

            x = stack.pop()
            # 일치하지 않는 경우
            if char == ')' and x != '(' or char == '}' and x != '{':
                return 0

    # 반복문 다 돌렸는데 stack 에 괄호가 남아있는 경우
    return 0 if stack else 1


for t in range(1, int(input())+1):
    print(f'#{t} {solution(input())}')
