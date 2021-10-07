# git commit -m "code: Solve swea L5247 연산 (seungkyu)"
import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(n):
    visited = [0]*1000001
    q  = deque()
    visited[n] = 1
    q.append((n, 0))

    while q:
        n, cnt = q.popleft()
        if n == M:
            return cnt
        if n+1 < 1000001 and not visited[n+1]:
            visited[n+1] = 1
            q.append((n+1, cnt+1))
        if n-1 > 0 and not visited[n-1]:
            visited[n-1] = 1
            q.append((n-1, cnt+1))
        if n*2 < 1000001 and not visited[n*2]:
            visited[n*2] = 1
            q.append((n*2, cnt+1))
        if n-10 > 0 and not visited[n-10]:
            visited[n-10] = 1
            q.append((n-10, cnt+1))

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    ans = bfs(N)

    print(f'#{tc} {ans}')