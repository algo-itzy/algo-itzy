# git commit -m "code: Solve boj 01918 후위 표기식 (seungjoo)"
import sys
input = sys.stdin.readline

s = input().rstrip()
stack = [] 
answer = ''

for char in s:
    if char.isalpha():
        answer += char
    else:
        if char == '(':
            stack.append(char)
        elif char == '*' or char == '/':          
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(char)
        elif char == '+' or char == '-':          
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(char)
        elif char == ')':                         
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()
print(answer)