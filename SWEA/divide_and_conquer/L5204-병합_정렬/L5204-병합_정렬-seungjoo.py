# git commit -m "code: Solve swea L5204 병합 정렬 (seungjoo)"
def merge_arr(left_arr, right_arr):
    global answer
    if left_arr[-1] > right_arr[-1]:
        answer += 1
    merge_arr = []
    left_idx, right_idx = 0, 0
    n, m = len(left_arr), len(right_arr)

    while left_idx != n and right_idx != m:
        if left_arr[left_idx] <= right_arr[right_idx]:
            merge_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merge_arr.append(right_arr[right_idx])
            right_idx += 1

    if left_idx != n:
        merge_arr += left_arr[left_idx:]
    if right_idx != m:
        merge_arr += right_arr[right_idx:]

    return merge_arr

def divide_arr(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = divide_arr(a[:mid])
    right = divide_arr(a[mid:])
    return merge_arr(left, right)


for test in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    arr = divide_arr(arr)
    print(f'#{test} {arr[N//2]} {answer}')