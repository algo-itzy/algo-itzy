import sys
sys.stdin = open('input.txt')


def quick_sort(left, right):
    if left >= right:
        return

    pivot = left
    i = left + 1
    j = right - 1

    while i <= j:
        while i <= j and data[pivot] >= data[i]:
            i += 1
        while i <= j and data[pivot] <= data[j]:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]

    data[pivot], data[j] = data[j], data[pivot]

    quick_sort(left, j)
    quick_sort(j+1, right)


for t in range(1, int(input())+1):
    N = int(input())
    data = list(map(int, input().split()))
    quick_sort(0, len(data))
    print(f'#{t} {data[N//2]}')
