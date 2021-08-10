from collections import deque


def bfs(n):
    q = deque([n])
    infected[n] = 1

    while q:
        x = q.popleft()

        for w in graph[x]:
            if not infected[w]:
                q.append(w)
                infected[w] = 1

    return infected


n = int(input())
graph = [[] for _ in range(n+1)]
infected = [0] * (n+1)

for _ in range(int(input())):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

print(sum(bfs(1))-1)

"""
기본적인 bfs 문제
"""