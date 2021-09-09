# 1 익은, 0 익지 않은, 01 없음
 
import sys
from collections import deque

input = sys.stdin.readline
m,n,h = map(int, input().split())

li=[[list(map(int, input().split())) for i in range(n)] for box in range(h)]

dx = [1, -1, 0, 0, 0, 0]        # 상하좌우 + 위아래
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1] 
res = 0                         # 시간 담는 변수

def bfs():
    global res  # 함수 밖의 변수가 global 해줘야 함 

    while queue:
        z,x,y,tmp = queue.popleft()

        for i in range(6):
            nx= x + dx[i]
            ny= y + dy[i]
            nz= z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and li[nz][nx][ny] == 0: # 상자 범위 안에 있고, 토마토가 아직 안 익었으면
                li[nz][nx][ny]= li[z][x][y] + 1
                res= tmp + 1 
                queue.append([nz, nx, ny, tmp+1])


queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if li[i][j][k] ==  1 :
                queue.append([i,j,k,0]) # 처음 queue 에 넣는 값들은 이미 1이므로 시간은 0

bfs()

def func(res):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if li[i][j][k] == 0:    # 0 이 하나라도 있으면 실패
                    print(-1)
                    return 
    print(res)                          # 위에서 return 안 한 경우, 저장된 시간의 변수를 출력 
    return  

func(res)

# git commit -m "code: Solve boj 07569 토마토 (yeonju)"