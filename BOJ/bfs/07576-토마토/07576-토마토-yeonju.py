# 익은 토마토는 익지 않은 토마토에 영향을 
# 익은 토마토 1, 익지 앟은 토마토 0, 토마토 x -1
# 저장될 때부터 모든 토마토 익어있으면 0, 토마토가 모두 익지 못하면 -1
import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4): 
            n_dx = x+ dx[i]
            n_dy = y + dy[i]

            if 0<= n_dx < n and 0 <= n_dy < m and arr[n_dx][n_dy] ==0: # 상하좌우 0인 토마토는 영향 받기
                queue.append([n_dx, n_dy])
                arr[n_dx][n_dy] = arr[x][y] +1 
                 

m, n = map(int, input().split()) # 가로 칸 수 m, 세로 칸 수 n

arr = [list(map(int, input().split()) for i in range(n))] 
queue = deque()

dx = [-1, 1, 0, 1]
dy = [0, 0, -1, 1]

res = 0

for i in range(n):
    for j in range(m):
        if arr[i][j]==1: # 익은 토마토가 있는 위치를 queue 에 추가 
            queue.append([i,j])

bfs()

isTrue = False
ans = -2

for i in arr:
    for j in i:
        if j == 0:
            isTrue = True
        ans = max(ans,j)

if isTrue == True:
    print(-1)
else:
    print(ans-1)


# git commit -m "Solve boj 07576 토마토 (yeonju)"

