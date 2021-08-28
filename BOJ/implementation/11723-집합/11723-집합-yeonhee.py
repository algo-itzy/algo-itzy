import sys
input = sys.stdin.readline

M = int(input())
S = set()
S_all = set(map(str, range(1, 21)))

for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'add':
        S.add(cmd[1])
    elif cmd[0] == 'remove':
        S.discard(cmd[1])
    elif cmd[0] == 'check':
        print(1 if cmd[1] in S else 0)
    elif cmd[0] == 'toggle':
        S.discard(cmd[1]) if cmd[1] in S else S.add(cmd[1])
    elif cmd[0] == 'all':
        S = S_all
    elif cmd[0] == 'empty':
        S = set()

"""
S_all 안하면 시간초과 나네요...
"""
