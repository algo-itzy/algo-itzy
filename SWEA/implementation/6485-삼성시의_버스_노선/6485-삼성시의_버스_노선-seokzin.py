T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * 5001
    res = []

    for _ in range(N):
        a, b = map(int, input().split())

        for i in range(a, b+1):
            arr[i] += 1

    for _ in range(int(input())):
        res.append(arr[int(input())])

    print(f"#{tc}", *res)

# 색칠하기 문제처럼 arr에 카운트를 누적했습니다.