import sys
input = sys.stdin.readline
from collections import deque


def BFS(x,y):
    queue = deque()
    queue.append([x,y])
    matrix[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny]==1:
                matrix[nx][ny] = matrix[x][y]+1
                queue.append([nx,ny])


N,M = map(int,input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

BFS(0,0)
print(matrix[N-1][M-1])