# git commit -m "code: Solve swea L5207 이진 탐색 (seungkyu)"
def binary_search(l, r, num):
    global cnt
    flag = 0

    while l <= r:
        m = (l+r) // 2
        if numbers[m] == num:
            cnt += 1
            return
        elif numbers[m] > num:  # 왼
            if flag == 1:
                return
            r = m-1
            flag = 1
        elif numbers[m] < num:   # 오
            if flag == 2:
                return
            l = m+1
            flag = 2


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    b = list(map(int, input().split()))
    cnt = 0

    for num in b:
        binary_search(0, len(numbers)-1, num)

    print(f'#{tc} {cnt}')
