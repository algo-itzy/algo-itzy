# git commit -m "code: Solve swea L5204 병합 정렬 (jiwoong)"
def mergeSort(low, high):
    global ans
    if low == high:
        return
    mid = (low + high + 1) // 2
    mergeSort(low, mid - 1)
    mergeSort(mid, high)
    if ai[mid - 1] > ai[high]:
        ans += 1
    i, j, k = low, mid, low
    while i <= mid - 1 and j <= high:
        if ai[i] <= ai[j]:
            arr[k] = ai[i]
            k, i = k + 1, i + 1
        else:
            arr[k] = ai[j]
            k, j = k + 1, j + 1
    while i <= mid - 1:
        arr[k] = ai[i]
        k, i = k + 1, i + 1
    while j <= mid:
        arr[k] = ai[j]
        k, j = k + 1, j + 1
    for x in range(low, high + 1):
        ai[x] = arr[x]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    arr = [0] * N
    ans = 0
    mergeSort(0, N - 1)
    print('#{} {} {}'.format(tc, ai[N // 2], ans))
