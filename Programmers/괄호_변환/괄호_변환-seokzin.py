def solution(p):
    if not p:
        return ""

    u, v = div(p)

    if check(u):
        return u + solution(v)
    else:
        res = f'({solution(v)})'

        # swap 방식으로 4-4 처리
        u = u.replace('(', '*')
        u = u.replace(')', '(')
        u = u.replace('*', ')')
        
        res += u[1:-1]

        return res


def div(p):
    l, r = 0, 0

    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1

        if l == r:
            return p[:i+1], p[i+1:]
    
    
def check(p):
    stack = []

    for x in p:
        if x == '(':
            stack.append(x)
        else:
            if not stack:
                return 0
            elif stack[-1] == '(':
                stack.pop()

    return 0 if stack else 1