import sys
input = sys.stdin.readline

n = int(input())
S = set()
numbers = (i for i in range(1,21))  # 미리 안만들고 하면 시간초과..
for _ in range(n):
    cmd = input().split()
        
    if cmd[0] == 'add':
        S.add(int(cmd[1]))

    elif cmd[0] == 'remove':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))

    elif cmd[0] == 'check':
        if int(cmd[1]) in S:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'toggle':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.add(int(cmd[1]))

    elif cmd[0] == 'all':
        S = set(numbers)

    elif cmd[0] == 'empty':
        S = set()
