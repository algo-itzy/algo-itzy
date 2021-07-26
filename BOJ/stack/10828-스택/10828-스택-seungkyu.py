# 입출력 속도 sys.stdin.readline > raw_input() > input()
# 스택 구조 => 파이썬 리스트 활용해서 구현 가능
import sys
N = int(sys.stdin.readline())
# len함수는 O(n) 시간 복잡도를 가질 것 같아 size 변수를 만들어봄
size = 0
stack_list = []
for _ in range(N):
    # input() 사용시 시간 초과됨
    command = sys.stdin.readline().split()
    # push 일때만 command[1]이 존재
    if command[0] == 'push':
        stack_list.append(command[1])
        size += 1
    elif command[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            # list.pop() => 제일 뒤의 원소가 빠져나옴
            print(stack_list.pop())
            size -= 1
    elif command[0] == 'top':
        if size == 0:
            print(-1)
        else:
            # 제일 뒤 원소 -1 인덱싱으로 쉽게 접근
            print(stack_list[-1])
    elif command[0] == 'size':
        print(size)
    elif command[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)