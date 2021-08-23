def inorder_tree(node,value):
    if node > N:
        return value
    else:
        value = inorder_tree(node*2,value)
        value += 1
        tree[node] = value
        value = inorder_tree(node*2 + 1,value)
        return value
 
for test in range(1, int(input())+1):
    N = int(input())
    tree = [0] *(N+1)
    inorder_tree(1,0)
    print(f'#{test} {tree[1]} {tree[N//2]}')