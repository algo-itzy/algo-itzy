def DFS(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            if not maze[nx][ny]:
                visited[nx][ny] = True
                if DFS(nx,ny):
                    return True
            elif maze[nx][ny] == 3:
                return True 


def find_start(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                return 1 if DFS(i,j) else 0


for test in range(1,int(input())+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    print(f'#{test} {int(find_start(N, maze))}')