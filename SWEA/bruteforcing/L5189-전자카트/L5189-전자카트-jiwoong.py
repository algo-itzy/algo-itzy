# git commit -m "code: Solve swea L5189 전자카트 (jiwoong)"
def check(t, s):
    if 0 not in visited:
        s += nums[t][0]
        global ans
        if ans == 0 or ans > s:
            ans = s
        pass
    else:
        for i in range(len(visited)):
            if visited[i] == 1:
                continue
            visited[i] = 1
            check(i, s + nums[t][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    visited = [0] * N

    visited[0] = 1
    check(0, 0)
    print('#{} {}'.format(tc, ans))
