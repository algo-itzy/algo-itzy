def solve():

    while 1:
        lenths = list(map(int, input().split()))
        # 길이가 0인 경우는 없으므로 lenths[0] 만 체크해도 될듯
        if lenths[0] == 0 and lenths[1] == 0 and lenths[2] == 0:
            break
        # 길이가 작은 2개 변 골라내기 위해 정렬
        lenths.sort()

        if lenths[0] ** 2 + lenths[1] ** 2 == lenths[2] ** 2:
            print("right")
        else:
            print("wrong")


if __name__ == "__main__":
    solve()
