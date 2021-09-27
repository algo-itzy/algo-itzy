# git commit -m "code: Solve swea L5202 화물 도크 (seungjoo)"
for test in range(1, int(input()) + 1):
    N = int(input())
    works = [tuple(map(int, input().split())) for _ in range(N)]
    works.sort(key=lambda x: (x[1], x[0]))
    last_finish = 0
    cnt = 0
    for s, e in works:
        if s >= last_finish:
            last_finish = e
            cnt += 1
    print(f'#{test} {cnt}')