import sys
sys.stdin = open('input.txt')


def dfs(s, g):
    stack = [s]
    visited = []

    while stack:
        x = stack.pop()
        if x not in visited:
            visited.append(x)
            stack.extend(graph[x])

    return 1 if g in visited else 0


for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)

    s, g = map(int, input().split())
    print(f'#{t} {dfs(s, g)}')
