# git commit -m "code: Solve boj 14502 연구소 (seungjoo)"
import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

def bfs(walls):
    q = deque()
    visited = [[False]*M for _ in range(N)]
    ret = 0
    for wall in walls:
        i, j = wall
        lab[i][j] = 1
    for v in virus:
        x, y = v
        q.append((x,y))
        visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not lab[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                ret += 1
    for wall in walls:
        i, j = wall
        lab[i][j] = 0
    return ret
        

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

cnt = 0
virus = []
candidates = []
for i in range(N):
    for j in range(M):
        if not lab[i][j]:
            candidates.append((i,j))
            cnt += 1
        elif lab[i][j]==2:
            virus.append((i,j))

max_area = 0
wall_sets = combinations(candidates,3)
for wall_set in wall_sets:
    max_area = max(cnt - bfs(wall_set)-3,max_area)
print(max_area)
