# git commit -m "code: Solve boj 15683 감시 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    visited[x][y] = True
    q.append((x,y,1))
    cnt = 1
    while q:
        x, y, key = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if matrix[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,key))
                    cnt += 1
                else:
                    if key:
                        visited[nx][ny] = True
                        q.append((nx,ny,0))
            
    return cnt+1

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

max_ans = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] and not visited[i][j]:
            max_ans = max(max_ans,bfs(i,j))
print(max_ans)