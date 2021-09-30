import sys
sys.stdin = open('input.txt')


def is_babygin(player, idx):
    if player[idx] == 3:
        return True
    if player[idx-2] and player[idx-1]:
        return True
    if player[idx-1] and player[idx+1]:
        return True
    if player[idx+1] and player[idx+2]:
        return True
    return False


for t in range(1, int(input())+1):
    numbers = list(map(int, input().split()))
    # 인덱스 오류 방지
    p1, p2 = {i: 0 for i in range(-2, 12)}, {i: 0 for i in range(-2, 12)}
    result = 0

    for i in range(12):
        if i % 2 == 0:
            p1[numbers[i]] += 1
            if is_babygin(p1, numbers[i]):
                result = 1
                break
        elif i % 2:
            p2[numbers[i]] += 1
            if is_babygin(p2, numbers[i]):
                result = 2
                break

    print(f'#{t} {result}')
