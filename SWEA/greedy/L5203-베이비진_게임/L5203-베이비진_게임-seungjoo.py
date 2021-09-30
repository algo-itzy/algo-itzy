# git commit -m "code: Solve swea L5203 베이비진 게임 (seungjoo)"
def check(player, num):
    if player[num] == 3:
        return True

    if num > 1 and player[num - 1] and player[num - 2]:
        return True
    if num < 9 and player[num + 1] and player[num + 2]:
        return True
    if num and not num==9 and player[num + 1] and player[num - 1]:
        return True
    return False


for test in range(1, int(input()) + 1):
    nums = list(map(int, input().split()))
    a = {i: 0 for i in range(10)}
    b = {i: 0 for i in range(10)}
    answer = 0
    flag = 0
    for i in range(len(nums)):
        if i&1:
            b[nums[i]] += 1
            if check(b, nums[i]):
                answer = 2
                break
        else:
            a[nums[i]] += 1
            if check(a, nums[i]):
                answer = 1
                break
    print(f'#{test} {answer}')