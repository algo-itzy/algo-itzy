# 처음에 input()으로 풀었으나 시간초과
# BOJ 15552번을 참고해 sys.stdin.readline로 수정

import sys
input = sys.stdin.readline

N = int(input())                 # 주어지는 명령의 수 N
stack = []                       # 비어있는 스택 정의

for _ in range(N):  
    cmd = input().split()        # 명령 리스트로 받음
    if cmd[0] == 'push':         # 정수 X를 스택에 넣는 연산
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':        # 가장 위에 있는 정수 빼고 출력. stack이 비어있을 경우 -1
        print(stack.pop() if stack else -1)
    elif cmd[0] == 'size':       # 스택에 들어있는 정수의 개수 출력
        print(len(stack))
    elif cmd[0] == 'empty':      # 비어있으면 1, 아니면 0
        print(0 if stack else 1)
    elif cmd[0] == 'top':        # 스택의 가장 위에 있는 정수 출력. stack이 비어있을 경우 -1
        print(stack[-1] if stack else -1)

