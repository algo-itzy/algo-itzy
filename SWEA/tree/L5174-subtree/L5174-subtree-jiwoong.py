def subtree(node):
    global ans
    if node != 0:
        ans += 1
        subtree(left[node])
        subtree(right[node])


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())  # N은 내가 원하는 루트
    arr = list(map(int, input().split()))

    left = [0] * (E + 2)  # 첫 번째 자식
    right = [0] * (E + 2)  # 두 번째 자식

    for i in range(E):
        paren, child = arr[i * 2], arr[2 * i + 1]
        if left[paren] == 0:
            left[paren] = child
        else:
            right[paren] = child

    ans = 0
    subtree(N)

    print(f'#{tc} {ans}')