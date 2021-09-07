N = int(input())
M = int(input())
S = input()

pattern = 0
cnt = 0
i = 1

while i < M - 1:
    if S[i - 1:i + 2] == 'IOI':
        pattern += 1
        if pattern == N:
            cnt += 1
            pattern -= 1
        i += 2
    else:
        pattern = 0
        i += 1

print(cnt)
