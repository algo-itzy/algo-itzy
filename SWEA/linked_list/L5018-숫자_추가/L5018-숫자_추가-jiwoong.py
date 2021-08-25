T = int(input())
for tc in range(1, T + 1):
    N, M, L = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    for _ in range(M):
        i, j = list(map(int, input().split()))
        nums.insert(i, j)

    print("#{0} {1}".format(tc, nums[L]))