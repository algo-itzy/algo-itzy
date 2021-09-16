# git commit -m "code: Solve boj 16928 뱀과 사다리 게임 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append((start,0))
    visited[start] = True
    while q:
        cur_node, cnt = q.popleft()
        for i in range(1,7):
            next_node = cur_node+i
            if next_node >= 100:
                return cnt+1
            if visited[next_node]:
                continue
            visited[next_node] = True
            if next_node in port:
                if not visited[port[next_node]]:
                    visited[port[next_node]] = True
                    q.append((port[next_node],cnt+1))
            else:
                q.append((next_node, cnt+1))


N, M = map(int, input().split())
visited = {i: False for i in range(1,101)}
port = {}
for _ in range(N+M):
    a, b = map(int, input().split())
    port[a] = b

print(bfs(1))