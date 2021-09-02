import sys
input = sys.stdin.readline

exp = input().split('-')

signs = exp[0].split('+')
ans = 0
for sign in signs:
    ans += int(sign)

for i in range(1, len(exp)):
    signs = exp[i].split('+')
    for sign in signs:
        ans -= int(sign)

print(ans)