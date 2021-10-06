# git commit -m "code: Solve swea L5207 이진 탐색 (jiwoong)"
def binary(left, right, target, dir):
    global ans
    if left > right:
        return
    mid = (left + right) // 2
    if A[mid] == target:
        ans += 1
        return
    elif A[mid] > target:  
        if dir == 1:
            return
        return binary(left, mid - 1, target, 1)
    elif A[mid] < target:  
        if dir == 2:
            return
        return binary(mid + 1, right, target, 2)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    ans = 0
    for target in B:
        if target in A:  
            binary(0, N - 1, target, 0)

    print('#{} {}'.format(tc, ans))
