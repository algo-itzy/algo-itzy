from collections import deque

for _ in range(int(input())):
    p = input()
    n = int(input())
    numbers = input().strip('[').strip(']').split(',')

    if n > 0:
        numbers = deque(map(int, numbers))

    result_flag = 0
    flag = 1

    for cmd in p:
        if cmd == 'D':
            if n == 0:
                print('error')
                result_flag = 1
                break
            else:
                if flag == 1:
                    numbers.popleft()
                    n -= 1
                elif flag == -1:
                    numbers.pop()
                    n -= 1
        elif cmd == 'R':
            flag *= -1

    if flag == -1:  # 시간초과 떄문에 마지막에 한번만 호출
        numbers.reverse()

    if not result_flag:
        print('[', ','.join(map(str, numbers)), ']', sep='')
