def heap_sort(node):
    mom_node = node//2
    if mom_node < 0:
        return
    else:
        if tree[mom_node] > tree[node]:
            tree[node], tree[mom_node] = tree[mom_node], tree[node]
            heap_sort(mom_node)



for test in range(1,int(input())+1):
    N = int(input())
    tree = [0]
    node_num = 1
    for num in map(int, input().split()):
        tree.append(num)
        heap_sort(node_num)
        node_num += 1
    sum_value = 0
    while N:
        N //= 2
        sum_value += tree[N]
        
    print(f'#{test} {sum_value}')