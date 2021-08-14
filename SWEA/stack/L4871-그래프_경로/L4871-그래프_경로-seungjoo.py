
def find_path(s,g):
    global answer
    if s==g:
        answer = 1
        return
    for next_node in graph[s]:
        if not visited[next_node]:
            visited[next_node] = True
            find_path(next_node,g)



for test in range(1,int(input())+1):
    V, E = map(int,input().split())
    graph = {i:[] for i in range(1,V+1)}
    answer = 0
    visited = {i:False for i in range(1,V+1)}
    for _ in range(E):
        a, b = map(int,input().split())
        graph[a] += [b]
    s,g = map(int,input().split())
    visited[s] = True
    find_path(s,g)
            
    print(f'#{test} {answer}')

