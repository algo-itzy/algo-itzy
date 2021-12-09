import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append((start, 0))
    dis = [-1] * (V + 1)
    dis[start] = 0

    while q:
        n, c = q.popleft()
        for nn, nc in graph[n]:
            if dis[nn] == -1:
                dis[nn] = c + nc
                q.append((nn, c + nc))

    result = max(dis)
    idx = dis.index(result)

    return idx, result


graph = defaultdict(list)
V = int(input())
for _ in range(V):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1, 2):
        graph[tmp[0]].append(tmp[i:i+2])

x = bfs(1)[0]

print(bfs(x)[1])
