# git commit -m "code: Solve boj 09663 N-Queen (seungjoo)"
import sys
input = sys.stdin.readline


def isTrue(x):
    for i in range(1, x):
        if check_row[x] == check_row[i] or abs(check_row[x] - check_row[i]) == x - i:
            return False
    return True


def dfs(cnt):
    global result
    if cnt > n:
        result += 1
    else:
        for i in range(1, n + 1):
            check_row[cnt] = i
            if isTrue(cnt):
                dfs(cnt + 1)

n = int(input())
check_row = [0 for _ in range(16)]
result = 0

dfs(1)

print(result)
