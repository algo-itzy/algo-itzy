# git commit -m "code: Solve boj 02263 트리의 순회 (seungjoo)"
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_tree(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return
    root = post_order[post_right]
    root_idx = in_order_idx[root]
    pre_order.append(root)
    left_size = root_idx - in_left
    find_tree(in_left, root_idx - 1, post_left, post_left + left_size - 1)
    find_tree(root_idx + 1, in_right, post_left + left_size, post_right - 1)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_order_idx = {in_order[i]: i for i in range(n)}
pre_order = []
find_tree(0, n - 1, 0, n - 1)
print(*pre_order)