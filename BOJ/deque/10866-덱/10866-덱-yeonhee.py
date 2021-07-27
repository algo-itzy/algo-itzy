import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

for _ in range(int(input())):    # input : test case
    cmd = input().split()        # input : command

    if cmd[0] == 'push_front':   # deque().appendleft()
        deq.appendleft(cmd[1]) 
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    elif cmd[0] == 'pop_front':  # depue().popleft()
        print(deq.popleft() if deq else -1) 
    elif cmd[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        print(0 if deq else 1)
    elif cmd[0] == 'front':
        print(deq[0] if deq else -1)
    elif cmd[0] == 'back':
        print(deq[-1] if deq else -1)

"""
이전 문제에서 deque 조금 써봤다고 금방 익숙해졌네요!
이런 류의 command 문제에서 명령어가 뭔지 적기 위해 else 안쓰고 굳이 elif 쓰고 있습니다.
"""