# 0 이 통로
# 1. 2의 위치 찾기
# 2. 2의 상하좌우에 0,3 이 있으면 이동 (단, 박스 범위 안에서)

def dfs(x,y):
    global ans                                         # 함수 밖에서도 이용해야하니, global 변수로 선언

    if maze[x][y] == 3:                                # 3을 발견하면 미로 탈출 성공 
        ans = 1
        return 
    
    visited.append((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
                                                        # 미로의 범위 안에 있고, 방문하지 않았고, 1이 아니면(0 or 3인 경우에만)
        if 0<= nx <n and 0<=ny <n and (nx,ny) not in visited and maze[nx][ny] != 1:
            dfs(nx, ny)


t = int(input())

for tc in range(t):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)] # 2차원 행열 미로 입력 받기 


    ans = 0                                            # 탈출 못했을 때의 기본값인 0으로 초기화
    visited =[]                                        # 방문했었는지 체크할 리스트 
    
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:                         # 시작점 위치 찾기 
                start_x, start_y =i,j


    dx = [0, 0, -1, 1]                                  # 상하좌우
    dy = [1, -1, 0, 0]

    dfs(start_x, start_y)                               

    if ans == 1:
        print(f'#{tc+1} 1')
    else: 
        print(f'#{tc+1} 0')

    











