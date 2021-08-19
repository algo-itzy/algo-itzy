import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    route = [0 for _ in range(200)]  # 이동 경로

    for _ in range(int(input())):
        s, e = map(int, input().split())

        # 방 번호를 0 ~ 199까지 숫자로 보정
        s = s//2 if s%2 else s//2 - 1
        e = e//2 if e%2 else e//2 - 1

        # s가 e보다 앞선 숫자가 되도록 조정
        if s > e:
            s, e = e, s

        # 이동 구간이 있을 경우 route 에 +1
        for i in range(s, e+1):
            route[i] += 1

    print(f'#{t} {max(route)}')
