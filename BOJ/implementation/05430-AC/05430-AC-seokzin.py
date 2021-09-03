for _ in range(int(input())):
    p = input()
    n = int(input())
    arr = input()

    if n == 0:
        arr = list()
    else:
        arr = list(map(int, arr.replace('[', '').replace(']', '').split(',')))

    flag = 0  # 뒤집기 체크 - 0 / -1

    for cmd in p:
        if cmd == 'R':
            flag = -1-flag
        elif cmd == 'D':
            if not arr:
                print('error')
                break
            else:
                arr.pop(flag) # pop(0), pop(-1)            
    else:
        arr = arr if not flag else arr[::-1]
        print('[', ','.join(map(str, arr)), ']', sep='')

# 진짜 문제 너무너무 지저분해.. 내가 어렵게 푼건가..?