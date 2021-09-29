# git commit -m "code: Solve swea L5202 화물 도크 (jiwoong)"
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: (-x[1], -x[0]))

    s, e = arr.pop()
    ans = 1
    while arr:
        ns, ne = arr.pop()
        if e <= ns:  # 현재 시작시간이 전회차의 끝시간보다 같거나 크면
            s, e = ns, ne  # 갱신
            ans += 1

    print("#{} {}".format(tc, ans))
