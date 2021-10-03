# git commit -m "code: Solve swea L5204 병합 정렬 (seungkyu)"
import sys
sys.stdin = open('input.txt')


def merge_sort(numbers):
    global cnt
    if len(numbers) == 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    if left[-1] > right[-1]:
        cnt += 1
    tmp = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    tmp += left[i:]
    tmp += right[j:]
    return tmp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    cnt = 0
    numbers = merge_sort(numbers)

    print(f'#{tc} {numbers[N//2]} {cnt}')
