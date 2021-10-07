# git commit -m "code: Solve swea L5248 그룹 나누기 (seungkyu)"
import sys
sys.stdin = open('input.txt')


def find_parent(num):
    if tree[num] < 0:
        return num
    else:
        return find_parent(tree[num])


def make_tree(tree, num1, num2):
    root1 = find_parent(num1)
    root2 = find_parent(num2)
    if root1 == root2:
        return
    if tree[root1] >= tree[root2]:
        tree[root1] += tree[root2]
        tree[root2] = root1
    else:
        tree[root2] += tree[root1]
        tree[root1] = root2


T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    tmp = []
    root = -1
    tree = [-1 for _ in range(N+1)]

    for i in range(0, len(nums), 2):
        make_tree(tree, nums[i], nums[i+1])

    ans = 0
    for num in tree:
        if num < 0:
            ans += 1
            
    print(f'#{tc} {ans-1}')
