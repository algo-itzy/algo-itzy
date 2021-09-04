def divide(n, s_x, s_y):  # 한변 크기, 시작 좌표
    global res
    if n == 0:
        return
    flag_0, flag_1 = 0, 0

    for i in range(s_x, s_x+n):
        for j in range(s_y, s_y+n):
            if not flag_1 and a[i][j]:
                flag_1 = 1
            elif not flag_0 and not a[i][j]:
                flag_0 = 1

    if not flag_0 and flag_1:  # 전부 1이면 1
        res += '1'
        return
    elif flag_0 and not flag_1:  # 전부 0이면 0
        res += '0'
        return
    elif flag_0 and flag_1:  # 0,1 섞이면 divide
        res += '('
        divide(n // 2, s_x, s_y)
        divide(n // 2, s_x, s_y + n // 2)
        divide(n // 2, s_x+n // 2, s_y)
        divide(n // 2, s_x+n // 2, s_y+n // 2)
        res += ')'


N = int(input())
a = [list(map(int, input())) for _ in range(N)]
res = ''
divide(N, 0, 0)
print(res)