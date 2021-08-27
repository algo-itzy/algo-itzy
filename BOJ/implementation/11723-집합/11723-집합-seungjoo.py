import sys
input = sys.stdin.readline

M = int(input())

S = {i:False for i in range(1,21)}
for _ in range(M):
    commands = input().split()

    if commands[0] == 'all':
        for i in range(1,21):
            S[i] = True
        continue
    elif commands[0] == 'empty':
        S = {i:False for i in range(1,21)}
        continue
    num = int(commands[1])
    if commands[0] == 'add':
        if not S[num]:
            S[num] = True
    elif commands[0] == 'remove':
        if S[num]:
            S[num] = False
    elif commands[0] == 'toggle':
        S[num] = False if S[num] else True
    elif commands[0] == 'check':
        print(1 if S[num] else 0)