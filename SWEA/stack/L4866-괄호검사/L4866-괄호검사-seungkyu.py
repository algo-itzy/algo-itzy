import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    
    ans = 1
    words = input()
    stack_bracket = []

    for word in words:
        # ( 나 { 올 때는 append
        if word == '(':
            stack_bracket.append('(')
        elif word == '{':
            stack_bracket.append('{')

        elif word == ')':
            if len(stack_bracket) == 0:  # 이미 스택이 비어있으면 false
                ans = 0
                break
            elif stack_bracket[-1] == '(':
                stack_bracket.pop()
            else:
                ans = 0
                break

        elif word == '}':
            if len(stack_bracket) == 0:  # 이미 스택이 비어있으면 false
                ans = 0
                break 
            elif stack_bracket[-1] == '{':
                stack_bracket.pop()
            else:
                ans = 0
                break

    if stack_bracket:
        ans = 0

    print(f'#{test_case} {ans}')