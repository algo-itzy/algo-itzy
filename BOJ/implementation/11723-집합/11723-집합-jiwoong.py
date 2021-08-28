import sys

input = sys.stdin.readline

S = set()
M = int(input())
for i in range(M):
    op = input().split()

    if op[0] == 'add':
        S.add(int(op[1]))

    elif op[0] == 'remove':
        if int(op[1]) in S:
            S.remove(int(op[1]))

    elif op[0] == 'check':
        if int(op[1]) in S:
            print(1)
        else:
            print(0)

    elif op[0] == 'toggle':
        if int(op[1]) in S:
            S.remove(int(op[1]))
        else:
            S.add(int(op[1]))

    elif op[0] == 'all':
        S = {i for i in range(1, 21)}

    elif op[0] == 'empty':
        S = set()
