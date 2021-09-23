T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    if str(N * (2 ** 12))[-1] != '0':
        print("#{} overflow".format(tc))
    else:
        m = int(N * (2 ** 12))
        tmp = ""
        for i in range(12):
            tmp += str(m % 2)
            m //= 2
        print("#{} {}".format(tc, str(int(tmp))[::-1]))
