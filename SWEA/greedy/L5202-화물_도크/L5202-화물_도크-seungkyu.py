# git commit -m "code: Solve swea L5202 화물 도크 (seungkyu)"
T = int(input())
for tc in range(1, T+1):

    times = []
    N = int(input())
    for _ in range(N):
        times.append(list(map(int, input().split())))

    times.sort(key=lambda x: (x[1], x[0]))
    cnt = 1
    i, j = times[0][0], times[0][1]
    for time in times:
        s, e = time[0], time[1]
        if j <= s:
            cnt += 1
            j = e

    print(f'#{tc} {cnt}')
