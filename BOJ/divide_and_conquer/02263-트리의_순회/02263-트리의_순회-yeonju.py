import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def search_preorder(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return

    root = postorder[post_right]

    root_idx = inorder_idx[root]
    preorder.append(root)
    left_side = root_idx - in_left

    search_preorder(in_left, root_idx - 1, post_left, post_left - 1 + left_side)
    search_preorder(root_idx + 1, in_right, post_left + left_side, post_right - 1)


n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

inorder_idx = {inorder[i]: i for i in range(n)}


search_preorder(0, n - 1, 0, n - 1)

print(*preorder)



# git commit -m "code: Solve boj 02263 트리의 순회 (yeonju)"