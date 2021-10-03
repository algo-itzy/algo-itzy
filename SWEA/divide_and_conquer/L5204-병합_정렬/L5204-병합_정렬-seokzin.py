def merge_sort(s):
    if len(s) <= 1:
        return s

    mid = len(s)//2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])

    return merge(left, right)


def merge(left, right):
    global cnt
    tmp = []
    i_l, i_r, n_l, n_r = 0, 0, len(left), len(right)

    if left[-1] > right[-1]:
        cnt += 1

    while i_l != n_l and i_r != n_r:
        if left[i_l] <= right[i_r]:
            tmp.append(left[i_l])
            i_l += 1
        else:
            tmp.append(right[i_r])
            i_r += 1

    if i_l == n_l:
        tmp += right[i_r:]
    elif i_r == n_r:
        tmp += left[i_l:]

    return tmp


for tc in range(1, int(input())+1):
    cnt = 0
    n = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc}', merge_sort(arr)[n//2], cnt)

# pop하여 임시 리스트에 append 개념이 이해는 쉬웠으나 시간 초과네요.
# 인덱스 이동 개념으로 리팩토링 하였습니다.