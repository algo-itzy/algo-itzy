# git commit -m "code: Solve swea L5205 퀵 정렬 (seungjoo)"
def quick_sort(a, left, right):
    if left < right:
        pivot = a[left]
        start = left + 1
        end = right
        while start <= end:
            while start <= end and a[start] <= pivot:
                start += 1
            while start <= end and a[end] >= pivot:
                end -= 1
            if start <= end:
                a[start], a[end] = a[end], a[start]
        a[left], a[end] = a[end], pivot
        mid = end
        quick_sort(a, left, mid - 1)
        quick_sort(a, mid + 1, right)


for test_case in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr) - 1)
    print(f'#{test_case} {arr[n//2]}')