import sys
from collections import deque
input = sys.stdin.readline

# 뒤집어질 때 제거를 위해 deque를 사용, 실제로 뒤집는 것은 마지막에만 진행
T = int(input())

for _ in range(T):
    reverse_flag = 0  # 뒤집어진 상태인지 표시 flag
    flag = 1  # error 관련 flag

    p = input().strip().replace('RR', '')  # 두번 연속 뒤집는 것은 원본과 같으므로 미리 제거
    n = int(input())
    num_input = input().strip().replace('[','').replace(']','').split(',')

    if n == 0:
        numbers = deque()  # 빈 리스트 주어졌을 때 예외처리
    else:
        numbers = deque(list(map(int, num_input)))

    for cmd in p:

        if cmd == 'R':
            if reverse_flag:
                reverse_flag = 0
            else:
                reverse_flag = 1

        elif cmd == 'D':
            if len(numbers) == 0:
                print("error")
                flag = 0
                break
            else:
                if reverse_flag:
                    numbers.pop()  # 뒤집혀진 상태에서는 오른쪽에서 제거
                else:
                    numbers.popleft()

    if flag:  # error 없을 때 뒤집혀있는지 확인 후 답 출력
        if reverse_flag:
            numbers.reverse()

        print('[', end='')
        for idx in range(len(numbers)):
            if idx < len(numbers)-1:
                print(numbers[idx], end=',')
            else:
                print(numbers[idx], end='')
        print(']')
