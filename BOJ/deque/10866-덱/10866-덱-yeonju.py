import sys
from collections import deque

N = int(sys.stdin.readline()) # 명령의 수

dq = deque()

for i in range(N) :
    cmd = list(input().split())

    if cmd[0] == "push_front" : # 정수를 덱의 앞에 넣기
        dq.appendleft(cmd[1])

    elif cmd[0] == "push_back" : # 정수를 덱의 뒤에 넣기
        dq.append(cmd[1])

    elif cmd[0] == "pop_front" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq.popleft()) # 덱의 가장 앞에 수를 빼기

    elif cmd[0] == "pop_back" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq.pop()) # 덱의 가장 뒤에 있는 수를 빼기

    elif cmd[0] == "size" :
        print(len(dq))

    elif cmd[0] == "empty" :
        if len(dq) == 0 :
            print(1)
        else :
            print(0)

    elif cmd[0] == "front" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[0]) # 덱의 가장 앞에 있는 수를 출력

    elif cmd[0] == "back" :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[-1]) # 덱의 가장 뒤의 수를 출력
