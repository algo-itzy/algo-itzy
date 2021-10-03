# 퀵정렬 : pivot 값을 기준으로 더 작은 값과 큰 값을 반복적으로 분할하여 정복하는 방식

def quick_sort(left, right):
    if left >= right:
        return

    pivot = left # 임의의 기준값 pivot
    i = left + 1
    j = right - 1

    while i <= j:
        # 왼쪽에서 오른쪽으로 이동한다. pivot 보다 값이 작은 경우
        while i <= j and a[i] <= a[pivot]:
            i += 1
        # 오른쪽에서 왼쪽으로 이동
        while i <= j and a[j] >= a[pivot]:
            j -= 1
        # 교차하지 않는 경우, 자리 바꾸기
        if i <= j:
            a[i], a[j] = a[j], a[i]
    # i 와 j가 교차하는 지점 - (j가 가리키는 값) (pivot) (i가 가리키는 값)
    # j 위치와 p pivot 위치의 값을 변경
    a[pivot], a[j] = a[j], a[pivot]

    quick_sort(left, j)
    quick_sort(j+1, right)


t = int(input())

for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    quick_sort(0, len(a))
    print(f'#{tc+1} {a[n//2]}')

# git commit -m "code: Solve swea L5205 퀵 정렬 (yeonju)"