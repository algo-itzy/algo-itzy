for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    flag1, flag2 = 0, 0
    res = 0

    for _ in range(6):
        c1 = arr.pop(0)
        c2 = arr.pop(0)

        p1[c1] += 1
        p2[c2] += 1

        if p1[c1] == 3:
            flag1 = 1

        for i in range(max(0, c1-2), min(c1+1, 8)):  # index out 방지
            if p1[i] and p1[i+1] and p1[i+2]:
                flag1 = 1

        if p2[c2] == 3:
            flag2 = 2

        for i in range(max(0, c2-2), min(c2+1, 8)):
            if p2[i] and p2[i+1] and p2[i+2]:
                flag2 = 2

        if flag1:
            res = flag1
            break

        if flag2:
            res = flag2
            break

    print(f"#{tc}", res)

# 1과 2가 같은 턴에 승리해도 먼저 완성한 1의 승리라고 한다... 참