import sys

input = sys.stdin.readline
N = int(input())  # N!


def fact(N):
    if N == 1:
        return 1
    else:  # factorial 구현
        num = N * fact(N - 1)
        return num


if N == 0:
    print(0)
else:
    num = str(fact(N))  # 문자열 처리로 0의 개수 count
    cnt = 0
    for i in range(len(num) - 1, -1, -1):  # 뒤에서부터 거꾸로
        if num[i] == "0":
            cnt += 1
        else:
            break
    print(cnt)
