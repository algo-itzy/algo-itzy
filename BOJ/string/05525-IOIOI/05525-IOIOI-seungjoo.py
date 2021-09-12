# git commit -m "code: Solve boj 05525 IOIOI (seungjoo)"
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip().replace('IO','*') + 'F'
flag = 0
cnt = 0
ans = 0
for char in S:
    if flag:
        if char=='*':
            cnt += 1
        else:
            if cnt >= N:
                if char=='I':
                    ans += 1
                ans += cnt - N
            cnt = 0
            flag = 0
    else:
        if char=='*':
            flag = 1
            cnt += 1
print(ans)