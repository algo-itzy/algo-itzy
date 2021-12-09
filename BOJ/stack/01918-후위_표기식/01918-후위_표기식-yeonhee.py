a = input()
stack = []
result = ''

for x in a:
    if x.isalpha():
        result += x
    else:
        if x == '(':
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        elif x in ('*', '/'):
            while stack and (stack[-1] in ('*', '/')):
                result += stack.pop()
            stack.append(x)
        elif x in ('+', '-'):
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(x)

while stack:
    result += stack.pop()

print(result)
