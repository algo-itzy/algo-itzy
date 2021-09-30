# git commit -m "code: Solve swea L5201 컨테이너 운반 (seungkyu)"
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)

    ans, j = 0, 0
    for i in range(N):
        if t[j] >= w[i]:
            ans += w[i]
            if j == M-1:
                break
            j += 1

    print(f'#{tc} {ans}')