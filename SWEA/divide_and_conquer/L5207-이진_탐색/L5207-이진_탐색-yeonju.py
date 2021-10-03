def binary_search():
    cnt = 0
    # B에 들어있는 m개의 정수들에 대해 A에 들어있는 수인지 확인
    for i in m_list:
        before = ''
        left = 0
        right = n - 1

        while left <= right:
            middle = (left + right) // 2

            if i == n_list[middle]:
                cnt += 1
                break

            elif i > n_list[middle]: # 오른쪽 탐색
                left = middle + 1
                now = 'right'

            elif i < n_list[middle]:   # 왼쪽 탐색
                right = middle - 1
                now = 'left'

            if before == now: # 번갈아 탐색한 게 아니면
                break
            before = now
    return cnt


tc = int(input())
for tc in range(tc):
    n, m = map(int, input().split())
    n_list = sorted(list(map(int,input().split()))) # 오름차순으로 정렬해줘야 함
    m_list = list(map(int, input().split()))
    print(f'#{tc+1} {binary_search()}')

# git commit -m "code: Solve swea L5207 이진 탐색 (yeonju)"