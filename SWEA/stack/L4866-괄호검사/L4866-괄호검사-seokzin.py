def is_vps(s):
    stack = [] # 괄호 담을 스택

    for c in s:
        if c == '(':
            stack.append('(')
        elif c == '{':
            stack.append('{')
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif c == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0
    
    return 1 if not stack else 0

T = int(input())

for tc in range(1, T+1):
    print(f"#{tc}", is_vps(input()))

# 백준 9012 괄호 풀이가 생각났습니다.