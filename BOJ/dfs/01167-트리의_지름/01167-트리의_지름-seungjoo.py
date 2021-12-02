# git commit -m "code: Solve boj 01167 트리의 지름 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque,defaultdict

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 0
    max_dist, max_node = 0, 0

    while queue:
        cur_node = queue.popleft()
        for next_node, next_dist in graph[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + next_dist
                queue.append(next_node)
                if max_dist < visited[next_node]:
                    max_dist, max_node = visited[next_node], next_node

    return max_dist, max_node

V = int(input())
graph = defaultdict(list)
visited = [-1] * (V + 1)

for _ in range(V):
    c = list(map(int, input().split()))
    for i in range(1, len(c) - 2, 2):
        graph[c[0]].append(c[i: i + 2])

dist, node = bfs(1)
dist, node = bfs(node)
print(dist)