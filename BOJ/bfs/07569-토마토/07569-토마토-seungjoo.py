# git commit -m "code: Solve boj 07569 토마토 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque

def bfs(red_tomatoes, tomato_cnt):
    day = -1
    while red_tomatoes:
        n = len(red_tomatoes)
        for _ in range(n):
            x,y,z = red_tomatoes.popleft()
            for dx,dy,dz in d:
                nx = x + dx
                ny = y + dy
                nz = z + dz
                if 0<=nx<N and 0<=ny<M and 0<=nz<H and not tomatoes[nz][nx][ny]:
                    red_tomatoes.append((nx,ny,nz))
                    tomatoes[nz][nx][ny] = 1
                    tomato_cnt += 1
        day += 1
    if tomato_cnt==M*N*H:
        return day
    else:
        return -1


M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

cnt = 0
q = deque()
for i in range(N):
    for j in range(M):
        for k in range(H):
            if tomatoes[k][i][j]==1:
                q.append((i,j,k))
                cnt += 1
            elif tomatoes[k][i][j]==-1:
                cnt += 1

d = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)]
print(bfs(q,cnt))