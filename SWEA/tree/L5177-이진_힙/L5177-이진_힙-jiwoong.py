T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    q = [0 for i in range(N + 1)]

    for i in range(1, N + 1):
        # q 삽입
        q[i] = nums[i - 1]
        heap = i
        while True:
            if q[heap] <= q[heap // 2] and heap != 1:
                q[heap], q[heap // 2] = q[heap // 2], q[heap]
            else:
                break
            heap //= 2

    ans = 0
    while N > 1:
        ans += q[N // 2]
        N //= 2

    print(f"#{tc} {ans}")