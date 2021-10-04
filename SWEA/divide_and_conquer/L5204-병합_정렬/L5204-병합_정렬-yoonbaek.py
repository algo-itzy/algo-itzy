def divide(start, end):
    if end-start == 1:
        return [nums[start]]
    mid = start + (end-start)//2
    left = divide(start, mid)
    right = divide(mid, end)
    
    return merge(left, right)


def merge(left, right):
    global cnt
    len_l, len_r = len(left), len(right)
    l, r = 0, 0
    tmp = []

    if left[-1] > right[-1]:
        cnt += 1

    while l < len_l and r < len_r:
        if left[l] <= right[r]:
            tmp.append(left[l])
            l += 1
        else:
            tmp.append(right[r])
            r += 1
    
    tmp += left[l:]
    tmp += right[r:]
            
    return tmp


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        nums = list(map(int, input().split()))
        cnt = 0

        sorted_list = divide(0, N)

        print(f"#{tc} {sorted_list[N//2]} {cnt}")

# git commit -m "code: Solve swea L5204 병합 정렬 (yoonbaek)"