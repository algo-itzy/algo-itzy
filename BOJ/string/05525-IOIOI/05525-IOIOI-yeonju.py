# 50점- 시간 초과

import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) # s 의 길이
s = input()

pn = 'IO'*n + 'I'
cnt = 0

for i in range(m-len(pn)+1):
    if pn == s[i:i+len(pn)]:
        cnt += 1

print(cnt)

# git commit -m "code: Solve boj 05525 IOIOI (yeonju)"