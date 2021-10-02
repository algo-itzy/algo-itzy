def merge_sort(s):
    if len(s) <= 1:
        return s

    mid = len(s)//2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])

    return merge(left, right)


def merge(left, right):
    global cnt
    tmp = [0] * (len(left) + len(right))
    i, i_l, i_r = 0, 0, 0

    if left[-1] > right[-1]:
        cnt += 1

    while i_l < len(left) or i_r < len(right):
        if i_l < len(left) and i_r < len(right):
            if left[i_l] <= right[i_r]:
                tmp[i] = left[i_l]
                i += 1
                i_l += 1
            else:
                tmp[i] = right[i_r]
                i += 1
                i_r += 1

        elif i_l < len(left):
            tmp[i] = left[i_l]
            i += 1
            i_l += 1

        elif right:
            tmp[i] = right[i_r]
            i += 1
            i_r += 1

    return tmp


for tc in range(1, int(input())+1):
    cnt = 0
    n = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc}', merge_sort(arr)[n//2], cnt)

# 임시 리스트에 append 개념이 이해는 쉬웠으나 시간 초과네요.
# 인덱스 이동 개념으로 리팩토링 하였습니다.