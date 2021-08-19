from collections import deque

def BFS(x,y):
    visited = [[-1]*N for _ in range(N)]
    visited[x][y] = 0
    queue = deque()
    queue.append([x,y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if not maze[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                elif maze[nx][ny]==3:
                    return visited[x][y]
    return 0

def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                result = BFS(i,j)
                return result

for test in range(1,int(input())+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer = find_start()
    print(f'#{test} {answer}')