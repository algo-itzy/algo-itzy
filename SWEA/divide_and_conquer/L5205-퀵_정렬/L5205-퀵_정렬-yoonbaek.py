def quick_sort(start, end):
    if start >= end:
        return

    pivot = nums[start]
    l, r = start+1, end-1

    while l <= r:
        while l <= r and nums[l] <= pivot:
                l += 1
        while l <= r and nums[r] >= pivot:
                r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]

    nums[start], nums[r] = nums[r], nums[start]        
    quick_sort(start, r)
    quick_sort(r+1, end)


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        nums = list(map(int, input().split()))

        quick_sort(0, N)

        print(f"#{tc} {nums[N//2]}")

# git commit -m "code: Solve swea L5205 퀵 정렬 (yoonbaek)"