import sys
sys.stdin = open('input.txt')


def merge_sort(lst):
    global cnt

    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left, right = merge_sort(lst[:mid]), merge_sort(lst[mid:])
    left_len, right_len = len(left), len(right)
    left_idx, right_idx = 0, 0

    result = []
    if left[-1] > right[-1]:
        cnt += 1

    while left_idx != left_len and right_idx != right_len:
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx == left_len:
        result.extend(right[right_idx:])
    elif right_idx == right_len:
        result.extend(left[left_idx:])

    return result


for t in range(1, int(input()) + 1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    print(f'#{t} {merge_sort(data)[N//2]} {cnt}')
