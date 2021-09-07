import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    N = int(input())  # 의상 수
    kinds = []  # 종류
    cnt = []  # 종류별 개수

    for _ in range(N):
        name, kind = input().split()
        if kind in kinds:  # 이미 cnt 했으면
            cnt[kinds.index(kind)] += 1
        else:  # 안했으면
            kinds.append(kind)
            cnt.append(1)

    ans = 1
    for i in cnt:
        ans *= i + 1
    ans -= 1
    print(ans)
