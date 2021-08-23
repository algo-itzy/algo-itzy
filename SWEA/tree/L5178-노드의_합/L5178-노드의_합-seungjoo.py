
def prefix_tree(node):
    if N-M < node <= N:
        return tree[node]
    elif node > N:
        return 0
    else:
        left = prefix_tree(node*2)
        right = prefix_tree(node*2 + 1)
        tree[node] = left + right
        return tree[node]
 
for test in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] *(N+1)
    for _ in range(M):
        node_num, value = map(int, input().split())
        tree[node_num] = value
    prefix_tree(1)
    print(f'#{test} {tree[L]}')

