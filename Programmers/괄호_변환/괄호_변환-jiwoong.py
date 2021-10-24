# git commit -m "code: Solve programmers 괄호 변환 (jiwoong)"
def solution(p):
    if p == '':
        return ''
    check = True
    if p[0] == ')':
        check = False
    left = 0  # '('
    right = 0  # ')'
    idx = 0
    for sign in p:
        idx += 1
        if sign == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    if check:
        return p[:idx] + solution(p[idx:])
    else:
        return '(' + solution(p[idx:]) + ')' + ''.join([')' if x == '(' else '(' for x in p[1:(idx - 1)]])
