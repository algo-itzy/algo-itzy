# git commit -m "code: Solve boj 13549 숨바꼭질 3 (seungkyu)"
import sys
input = sys.stdin.readline
from collections import deque
dist = [-1]*100001
n, k = map(int, input().split())
q = deque()
q.append(n)
dist[n] = 0
while q:
    x = q.popleft()
    for nx in [x+1, x-1, x*2]:
        if x == k:
            break
        if 0 <= nx < 100001:
            if nx == x*2 and dist[nx] == -1:
                dist[nx] = dist[x]
                q.appendleft(nx)
            elif dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
print(dist[k])