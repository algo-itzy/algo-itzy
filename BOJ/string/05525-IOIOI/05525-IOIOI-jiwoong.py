import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input())

cnt = 0
ans = 0
idx = 1

while idx < M-1:
    if S[idx-1] == 'I' and S[idx] == 'O' and S[idx+1] == 'I':
        cnt += 1
        if cnt == N:
            cnt -= 1
            ans += 1
        idx += 1
    else:
        cnt = 0
    idx += 1

print(ans)