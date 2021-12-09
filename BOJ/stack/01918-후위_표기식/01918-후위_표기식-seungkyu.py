# git commit -m "code: Solve boj 01918 후위 표기식 (seungkyu)"
import sys
input = sys.stdin.readline

isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

eqn = input().strip()
stack = []
res = ''

for tok in eqn:
    if tok.isalpha():
        res += tok
    else:
        if not stack:
            stack.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            while stack and isp[tok] <= isp[stack[-1]]:
                res += stack.pop()
            stack.append(tok)

while stack:
    res += stack.pop()

print(res)