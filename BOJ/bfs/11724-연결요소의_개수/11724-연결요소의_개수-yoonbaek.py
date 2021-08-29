# 11724번 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)
from collections import defaultdict, deque

ints = lambda : map(int, sys.stdin.readline().split())

# 976ms
def BFS(start):
    q = deque([start])
    visited[start-1] = 1

    while q:
        now = q.popleft()
        
        for next in graph[now]:
            if not visited[next-1]:
                visited[next-1] = 1
                q.append(next)

# 952ms
def DFS(start):
    s = deque([start])
    visited[start-1] = 1

    while s:
        now = s.pop()
        
        for next in graph[now]:
            if not visited[next-1]:
                visited[next-1] = 1
                s.append(next)

# 980ms
def DFS_recur(start):
    visited[start-1] = 1

    for next in graph[start]:
        if not visited[next-1]:
            visited[next-1] = 1
            DFS_recur(next)           


if __name__ == "__main__":
    N, M = ints()
    graph = defaultdict(list)
    visited = [0] * (N)

    for _ in range(M):
        u, v = ints()
        graph[u].append(v); graph[v].append(u)

    cnt = 0

    for v in range(N):
        if not visited[v]:
            # BFS(v+1)
            DFS_recur(v+1)
            cnt += 1

    print(cnt)
    
# git commit -m "code: Solve boj 11724 연결요소의 개수 (yoonbaek)"