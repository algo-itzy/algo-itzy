from collections import deque
import sys

# 입출력 속도 sys.stdin.readline > raw_input() > input()
n = int(sys.stdin.readline())
# len함수는 O(n) 시간 복잡도를 가질 것 같아 size 변수를 만들어봄
size = 0
# 큐  => 파이썬 deque 활용
# deque.popleft()와 deque.pop() 구별
queue = deque()
for _ in range(n):
    # input() 사용시 시간 초과됨
    command = sys.stdin.readline().split()
    # push_back, push_front 일때만 command[1]이 존재
    # push_back은 큐에서 새로운 원소 추가하는 방식
    if command[0] == 'push_back':
        queue.append(command[1])
        size += 1
    elif command[0] == 'push_front':
        # 0번 인덱스(제일 앞)에 새로운 원소를 집어넣으면서 뒤로 밀기
        queue.insert(0, command[1])
        size += 1
    elif command[0] == 'pop_front':
        if size == 0:
            print(-1)
        else:
            # deque.popleft() => 제일 앞의 원소가 빠져나옴
            print(queue.popleft())
            size -= 1
    elif command[0] == 'pop_back':
        if size == 0:
            print(-1)
        else:
            # deque.pop() => 제일 뒤의 원소가 빠져나옴
            print(queue.pop())
            size -= 1
    elif command[0] == 'front':
        if size == 0:
            print(-1)
        else:
            # 제일 앞 원소 인덱싱으로 쉽게 접근
            print(queue[0])
    elif command[0] == 'back':
        if size == 0:
            print(-1)
        else:
            # 제일 뒤 원소 -1 인덱싱으로 쉽게 접근
            print(queue[-1])
    elif command[0] == 'size':
        print(size)
    elif command[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
