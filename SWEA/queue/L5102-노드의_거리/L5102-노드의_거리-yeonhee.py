import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(s, g):
    global result
    queue = deque([s])
    visited[s] = 1

    while queue:
        tmp = queue.popleft()
        for w in graph[tmp]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[tmp] + 1
                if w == g:
                    result = visited[w] - 1  # 출발할 떄 1이 더해져서
                    return


for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = [[] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    result = 0

    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    s, g = map(int, input().split())
    bfs(s, g)

    print(f'#{t} {result}')
