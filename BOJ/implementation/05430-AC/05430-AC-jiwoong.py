def func(p, n):
    flag = 0  # 짝
    arr = [0, 0]
    # 홀수면 뒷 숫자, 짝수면 앞 숫자 삭제
    for s in p:
        if s == 'R' and flag == 0:
            flag = 1
        elif s == 'R' and flag == 1:
            flag = 0
        elif s == 'D' and flag == 0:
            arr[0] += 1
        elif s == 'D' and flag == 1:
            arr[1] += 1
        if sum(arr) > n:
            return 'error'

    # 삭제 후 reverse
    ans = nums[arr[0]:len(nums) - arr[1]]
    if flag:
        ans.reverse()
    return "["+",".join(ans)+"]"


T = int(input())
for tc in range(1, T+1):
    p = input()  # 연산
    n = int(input())  # 숫자 개수
    nums = input().lstrip('[').rstrip(']').split(',')

    print(func(p, n))