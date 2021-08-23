for test in range(1,int(input())+1):
    E, N = map(int, input().split())
    graph = {i:[] for i in range(1,E+2)}
    edge = list(map(int, input().split()))
    for i in range(0,2*E,2):
        graph[edge[i]] += [edge[i+1]]
    cnt = 1
    queue = []
    queue.append(N)
    while queue:
        cur_node = queue.pop()
        for next_node in graph[cur_node]:
            queue.append(next_node)
            cnt += 1
    print(f'#{test} {cnt}')
