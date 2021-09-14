# git commit -m "code: Solve boj 14500 테트로미노 (seungjoo)"
import sys
input = sys.stdin.readline

def dfs(x,y,depth,s,init_x,init_y):
    global max_sum
    if depth==4:
        max_sum = max(max_sum,s)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,depth+1,s+matrix[nx][ny],init_x,init_y)
            visited[nx][ny] = False
            if nx==init_x+2 and ny==init_y:
                if init_y-1>=0:
                    max_sum = max(s+matrix[nx][ny]+matrix[init_x+1][init_y-1],max_sum)
                if init_y+1<M:
                    max_sum = max(s+matrix[nx][ny]+matrix[init_x+1][init_y+1],max_sum)
            if nx==init_x and ny==init_y+2:
                if init_x+1<N:
                    max_sum = max(s+matrix[nx][ny]+matrix[init_x+1][init_y+1],max_sum)
                if init_x-1>=0:
                    max_sum = max(s+matrix[nx][ny]+matrix[init_x-1][init_y+1],max_sum)

    
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

max_sum = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,1,matrix[i][j],i,j)
        visited[i][j] = False
print(max_sum)