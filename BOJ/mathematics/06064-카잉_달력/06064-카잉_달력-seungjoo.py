# git commit -m "code: Solve boj 06064 카잉 달력 (seungjoo)"
def kaying(m, n, x, y):
    while x <= m * n:
        if not (x - y) % n:
            return x
        x += m
    return -1

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(kaying(m, n, x, y))