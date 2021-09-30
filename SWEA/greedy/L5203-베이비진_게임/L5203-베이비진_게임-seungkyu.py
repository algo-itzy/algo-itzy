# git commit -m "code: Solve swea L5203 베이비진 게임 (seungkyu)"
def check(nums, num):
    if nums[num] == 3:
        return True
    if nums[num+1] and nums[num+2]:
        return True
    if nums[num-1] and nums[num-2]:
        return True
    if nums[num-1] and nums[num+1]:
        return True    

    return False


T = int(input())
for tc in range(1, T+1):

    cards = list(map(int, input().split()))
    p1, p2 = {i: 0 for i in range(-2,12)}, {i: 0 for i in range(-2,12)}
    ans = 0
    for i in range(0, len(cards), 2):
        p1[cards[i]] += 1
        p2[cards[i+1]] += 1
     
        p1_check = check(p1, cards[i])
        p2_check = check(p2, cards[i+1])

        if p1_check:
            ans = 1
            break
        elif p2_check:
            ans = 2
            break

    print(f'#{tc} {ans}')