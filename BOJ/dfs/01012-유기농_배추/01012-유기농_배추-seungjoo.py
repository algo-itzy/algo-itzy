import sys
input = sys.stdin.readline
from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 사방탐색을 실시하고 
# 목표는 배추밭에서 근접한 배추를 check하고 0으로 돌려주는것.
def BFS(x,y):
    queue=deque()
    queue.append([x,y])
    radish[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 배추가 있으면 탐색
            if 0<=nx<N and 0<=ny<M and radish[nx][ny]:
                radish[nx][ny]=0
                queue.append([nx,ny])

# test횟수만큼 반복한다.
for test in range(1,int(input())+1):
    M,N,K = map(int,input().split())
    # 배추밭을 만든다.
    radish = [[0 for _ in range(M)] for _ in range(N)]
    # 배추를 심는다.
    for _ in range(K):
        x,y=map(int,input().split())
        radish[y][x]=1

    cnt=0
    for i in range(N):
        for j in range(M):
            if radish[i][j]==1: #배추가 있으면 탐색한다.
                BFS(i,j)
                cnt+=1          #탐색이 한번 끝날때마다 벌레를 한마리씩 늘린다.
    print(cnt)