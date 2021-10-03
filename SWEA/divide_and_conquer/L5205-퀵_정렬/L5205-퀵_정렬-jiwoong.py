# git commit -m "code: Solve swea L5205 퀵 정렬 (jiwoong)"
def quick_sort(left, right):
    if left >= right:
        return

    tmp = left
    i = left + 1
    j = right - 1
    while i <= j:
        while i <= j and a[tmp] >= a[i]:
            i += 1
        while i <= j and a[tmp] <= a[j]:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]

    a[tmp], a[j] = a[j], a[tmp]

    quick_sort(left, j)
    quick_sort(j + 1, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))

    quick_sort(0, len(a))
    print("#{} {}".format(tc, a[N // 2]))
