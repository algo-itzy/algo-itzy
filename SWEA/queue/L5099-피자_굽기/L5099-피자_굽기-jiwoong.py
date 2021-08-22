T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))
    pizza = [i for i in range(M)]

    q = pizza[0:N]

    while len(q) > 1:  # 마지막 피자까지
        if ci[q[0]] >= 1:  # 치즈 안녹았을 떄
            ci[q[0]] //= 2
            q.append(q.pop(0))  # rotate
        else:  # 다 녹았을 때
            q.pop(0)
            if N != M:  # 피자 다 안채워졌을 때
                q.append(pizza[N])
                N += 1

    last = q.pop() + 1

    print("#{} {}".format(tc, last))
