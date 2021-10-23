# git commit -m "code: Solve programmers 괄호 변환 (seungjoo)"
def solution(p):
    if not p: 
        return p
    n = len(p)
    left, right = 0, 0
    for i in range(n):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    u = p[:i+1]
    v = p[i+1:]
    stack = []
    for char in u:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                new_u = u[1:-1]
                tmp = ''
                for char in new_u:
                    if char == '(':
                        tmp += ')'
                    else:
                        tmp += '('
                return '(' + solution(v) + ')' + tmp
    else:
        return u + solution(v)