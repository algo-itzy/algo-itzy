import sys
input = sys.stdin.readline
from collections import deque


def BFS(x,y,cnt):
    queue = deque()
    matrix[x][y] = cnt
    count = 1
    visited[x][y] = True
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and matrix[nx][ny]==1 and not visited[nx][ny]:
                matrix[nx][ny] = cnt
                queue.append([nx,ny])
                count +=1
    return count

N = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []

for i in range(N):
    for j in range(N):
        if matrix[i][j]==1 and not visited[i][j]:
            cnt +=1
            answer.append(BFS(i,j,cnt))
            

l = len(answer)
print(l)
answer.sort()
for i in range(l):
    print(answer[i])