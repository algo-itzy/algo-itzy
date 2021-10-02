def quick_sort(left, right):
    if left >= right:
        return

    pivot = left
    i = left+1
    j = right-1

    while i <= j:
        while i <= j and s[pivot] >= s[i]: 
            i += 1

        while i <= j and s[pivot] <= s[j]: 
            j -= 1

        if i <= j:
            s[i], s[j] = s[j], s[i]

    s[pivot], s[j] = s[j], s[pivot]

    quick_sort(left, j)
    quick_sort(j+1, right)


for tc in range(1, int(input())+1):
    cnt = 0
    n = int(input())
    s = list(map(int, input().split()))

    quick_sort(0, len(s))
    
    print(f'#{tc}', s[n//2])

# 정석 코드라 따르긴 하지만 이 로직이 가장 효율적일까?