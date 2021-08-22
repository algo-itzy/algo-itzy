# 끄적거렸는데 조금 더 손을 봐야겠습니다,,, 완성해서 다시 올리겠습니다! 

# 1은 벽, 0은 통로
# 경로가 있으면 지나야하는 최소 칸의 수를, 경로 없으면 0 출력 

from collections import deque

def bfs(x,y):
    p = (x, y)
    queue = deque()
    queue.append(p)
    visited[x][y] = 1
    cnt = 0

    while queue:
        i, j = queue.popleft()

        if maze[i][j] ==3:
            return visited[i][j] 
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
        
            if 0<= nx < n and 0 <= ny <n and maze[nx][ny] != 1 and (nx,ny) not in visited:
                queue.append(nx, ny)
                visited[nx][ny] = visited[i][j] + 1

    return 2

t = int(input())

for tc in range(t):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    queue = []

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2: # 시작점을 찾는다면 
                start_x, start_y =i, j

    dx = [0, 0, -1, 1]                                  # 상하좌우
    dy = [1, -1, 0, 0]
    
    visited =[[0]* (n+1) for _ in range(n+1)]

  


