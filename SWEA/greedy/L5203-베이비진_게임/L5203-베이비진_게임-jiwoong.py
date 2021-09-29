# git commit -m "code: Solve swea L5203 베이비진 게임 (jiwoong)"
def babygjn(num, cnt):  # 카드숫자, 카운팅리스트
    cnt[num] += 1
    tmp = 0
    i = 0
    while i < 8:
        if cnt[i] >= 3:  # babygjn check
            tmp = 1
            break
        if cnt[i] and cnt[i + 1] and cnt[i + 2]:  # run check
            tmp = 1
            break
        i += 1
    if tmp == 1:
        return True


T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    p1, p2 = [0] * 10, [0] * 10

    ans = 0
    for i in range(0, len(cards), 2):
        if babygjn(cards[i], p1):
            ans = 1
            break
        if babygjn(cards[i + 1], p2):
            ans = 2
            break

    print("#{} {}".format(tc, ans))
