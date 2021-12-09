# git commit -m "code: Solve boj 01918 후위 표기식 (jiwoong)"
import sys

input = sys.stdin.readline

infix = input().rstrip('\n')
postfix = ''
stack = []

for i in infix:
    if i.isalpha():
        postfix += i
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.append(i)
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            postfix += stack.pop()
        stack.append(i)
while stack:
    postfix += stack.pop()

print(postfix)
