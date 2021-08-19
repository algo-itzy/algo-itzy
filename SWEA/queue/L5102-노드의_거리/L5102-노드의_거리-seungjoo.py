
from collections import deque

def BFS(start,goal):
    queue = deque()
    queue.append([start,0])
    visited = {i: False for i in range(1,V+1)}
    visited[start] = True
    while queue:
        cur_node, cur_dist = queue.popleft()
        if cur_node==goal:
            return cur_dist
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append([next_node,cur_dist+1])
    return 0

for test in range(1,int(input())+1):
    V, E = map(int, input().split())
    graph = {i: [] for i in range(1,V+1)}
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a] += [b]
        graph[b] += [a]
    S, G = map(int, input().split())
    answer = BFS(S, G)
    print(f'#{test} {answer}')