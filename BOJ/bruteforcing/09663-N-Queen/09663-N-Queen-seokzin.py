def pos(x):  # 배치 가능성 검증
    for i in range(1, x):
        if s[x]==s[i] or abs(s[x]-s[i]) == x-i:
            return 0
    return 1


def dfs(idx):
    global res

    if idx > n:
        res += 1
        return

    for i in range(1, n+1):
        s[idx] = i
        if pos(idx):
            dfs(idx+1)


n = int(input())
s = [0] * (n+1)
res = 0

dfs(1)

print(res)
