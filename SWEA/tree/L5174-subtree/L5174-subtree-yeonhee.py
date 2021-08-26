import sys
from collections import deque

sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))
    graph = {i: [] for i in range(1, E+2)}
    visited = [0] * (E+2)

    for i in range(0, 2*E, 2):
        graph[nums[i]] += [nums[i+1]]

    # bfs
    q = deque([N])
    visited[N] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            q.append(next)
            visited[next] = 1

    print(f'#{t} {sum(visited)}')
