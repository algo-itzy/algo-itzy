# git commit -m "code: Solve boj 10026 적록색약 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y,color):
    visited[x][y] = True
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and picture[nx][ny]==color and not visited[nx][ny]:
                visited[nx][ny]= True
                q.append([nx,ny])

def bfs2(x,y):
    visited[x][y] = True
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and (picture[nx][ny]=='R' or picture[nx][ny]=='G') and not visited[nx][ny]:
                visited[nx][ny]= True
                q.append([nx,ny])


N = int(input())
picture = [list(input().rstrip()) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

color = {'R': 0, 'G': 0, 'B': 0}
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j,picture[i][j])
            color[picture[i][j]] += 1

ans = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and (picture[i][j]=='R' or picture[i][j]=='G'):
            bfs2(i,j)
            ans += 1
print(color['R']+color['G']+color['B'],ans+color['B'])