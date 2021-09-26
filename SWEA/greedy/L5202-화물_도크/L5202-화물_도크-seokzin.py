for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]))
    res = 0
    last = 0  # 마지막 회의 종료 시간

    for s, e in arr:
        if s >= last:
            res += 1
            last = e

    print(f"#{tc}", res)

# 회의실 배정 문제랑 똑같음