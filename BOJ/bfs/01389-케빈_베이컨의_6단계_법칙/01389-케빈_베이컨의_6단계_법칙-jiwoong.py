import sys
from collections import deque

input = sys.stdin.readline


def BFS(j):
    visited = [0] * (N + 1)
    q.append(j)
    visited[j] = 1
    while q:
        i = q.popleft()
        for j in arr[i]:
            if not visited[j]:
                visited[j] = visited[i] + 1
                q.append(j)
    return sum(visited)


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

q = deque()
ans = []
for i in range(1, N + 1):
    ans.append(BFS(i))

print(ans.index(min(ans)) + 1)
