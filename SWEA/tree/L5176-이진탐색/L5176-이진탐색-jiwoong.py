def inorder(root):
    global num
    if 1 <= root <= N:
        # 왼쪽
        left = root * 2
        if 0 < left < N + 1:
            inorder(left)
        tree[root] = num
        num += 1
        # 오른쪽
        right = root * 2 + 1
        if 0 < right < N + 1:
            inorder(right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)

    num = 1
    inorder(1)
    print(f"#{tc}", tree[1], tree[N // 2])
