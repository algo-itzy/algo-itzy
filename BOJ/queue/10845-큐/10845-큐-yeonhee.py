import sys
from collections import deque

input = sys.stdin.readline
que = deque()

for _ in range(int(input())):  # input : test case
    cmd = input().split()      # input : command

    if cmd[0] == 'push':
        que.append(cmd[1])
    elif cmd[0] == 'pop':      # deque의 popleft()를 이용해 맨 앞에 있는 값 제거
        print(que.popleft() if que else -1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        print(0 if que else 1)
    elif cmd[0] == 'front':
        print(que[0] if que else -1) 
    elif cmd[0] == 'back':
        print(que[-1] if que else -1)

"""
저번 문제에 썼던 deque가 너무 편리해서 또 썼습니다 :)
시간 초과 날 일이 없네요.......
"""