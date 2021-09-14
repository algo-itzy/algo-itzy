# git commit -m "code: Solve boj 17626 Four Squares (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append((n,0))
    visited[n] = True
    while q:
        r, cnt = q.popleft()
        flag = 1
        for square in squares:
            next_r = r-square
            if next_r > 0 and not visited[next_r]:
                if flag:
                    first = next_r
                    flag = 0
                if first > square and next_r>=4:
                    break
                visited[next_r] = True
                q.append((next_r,cnt+1))
            elif next_r == 0:
                return cnt + 1
                
n = int(input())
squares = []
m = int(50000*0.5)
for i in range(m,0,-1):
    squares.append(i**2)
visited = {i: False for i in range(n+1)}
print(bfs(n))