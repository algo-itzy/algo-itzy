# git commit -m "code: Solve swea L5208 전기버스2 (jiwoong)"
def dfs(i, stop, fuel):  # 현재 위치, 최대 범위, 교환 횟수
    global ans
    if fuel >= ans:
        return
    if stop >= N:
        ans = min(fuel, ans)
        return
    for j in range(stop, i, -1):
        dfs(j, j + M[j], fuel + 1)


T = int(input())
for tc in range(1, T + 1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    M = [0] + tmp[1:]  # 정류장 별 배터리 용량(1~N-1)

    ans = 10000
    dfs(1, 1 + M[1], 0)
    print("#{} {}".format(tc, ans))
