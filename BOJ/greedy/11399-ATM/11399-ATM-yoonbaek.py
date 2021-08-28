# 어르신들 버스 내리실 때 모습 생각하면서 풀었습니다.

if __name__ == "__main__":
    N = int(input())
    Ps = sorted(list(map(int, input().split())))

    # time per person
    tpp, total = 0, 0
    for p in Ps:
        tpp += p
        total += tpp

    print(total)
