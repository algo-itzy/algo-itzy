# git commit -m "code: Solve swea L5207 이진 탐색 (seungjoo)"
for test in range(1, int(input()) + 1):
    N,  M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    answer = 0
    for num in B:
        left, right, flag = 0, N - 1, 2
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == num:
                answer += 1
                break
            if num < A[mid]:
                right = mid - 1
                if flag == 1: break
                flag = 1
            elif num > A[mid]:
                left = mid + 1
                if not flag: break
                flag = 0
    print(f'#{test} {answer}')