# git commit -m "code: Solve swea L5205 퀵 정렬 (seungkyu)"
def quick_sort(arr, start, end):
    if start >= end: 
        return

    pivot = start 
    left = start + 1
    right = end

    while(left <= right):

        while(left <= end and arr[left] <= arr[pivot]):
            left += 1

        while(right > start and arr[right] >= arr[pivot]):
            right -= 1

        if(left > right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, N-1)

    print(f'#{tc} {numbers[N//2]}')
