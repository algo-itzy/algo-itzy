T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    for i in range(N - M, 0, -1):
        if i * 2 <= N:
            tree[i] = tree[i * 2]
            if i * 2 + 1 <= N:
                tree[i] += tree[i * 2 + 1]

    print(f'#{tc} {tree[L]}')
