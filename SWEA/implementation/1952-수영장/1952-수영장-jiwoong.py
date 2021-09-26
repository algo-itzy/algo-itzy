# git commit -m "code: Solve swea 1952 수영장 (jiwoong)"
def dfs(mon, acc):
    global ans
    if mon == 13:
        if ans > acc:
            ans = acc
        return
    if mon < 13:
        dfs(mon + 1, acc + plan[mon] * d)
        dfs(mon + 1, acc + m)
        dfs(mon + 3, acc + q)


T = int(input())
for tc in range(1, T + 1):
    d, m, q, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    ans = y
    dfs(1, 0)
    print("#%d" % tc, ans)
