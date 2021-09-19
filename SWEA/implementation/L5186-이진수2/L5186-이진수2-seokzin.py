for tc in range(1, int(input())+1):
    num = float(input())
    div = 1/2
    res = ''

    for _ in range(12):
        if num == 0:
            break

        elif num >= div:
            res += '1'
            num -= div
            div /= 2
        else:
            res += '0'
            div /= 2

    if num > 0:
        res = 'overflow'

    print(f"#{tc}", res)
