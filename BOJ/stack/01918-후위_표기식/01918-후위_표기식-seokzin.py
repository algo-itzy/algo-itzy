s = input()
stack = []
res = ""

for c in s:
    if c.isalpha():
        res += c
    else:
        if c == '(':
            stack.append(c)
        elif c == '*' or c =='/':
            while stack and stack[-1] in '*/':
                res += stack.pop()
            stack.append(c)
        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop() # '(' 제거

while stack:
    res += stack.pop()

print(res)