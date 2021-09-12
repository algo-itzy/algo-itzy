for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    while x <= m*n:
        if x%n == y%n:  # y%n인 이유는 x가 n의 배수일 때 때문
            print(x)
            break
        else:
            x += m
    else:
        print(-1)  # 탐색 실패시

# 더 개선할 수 있다고 생각하지만 패쓰