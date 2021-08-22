# 시작점 2
def StartPoint(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return [i, j]


def DFS(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 방문 기록을 가진 visited
    if not visited[x][y]:
        visited[x][y] = True

        # 우, 좌, 하, 상
        for xi, yi in zip(dx, dy):
            new_x = x + xi
            new_y = y + yi
            # 미로 나가지 말고
            if 0 <= new_x < N:
                if 0 <= new_y < N:
                    # 3 도착
                    if maze[new_x][new_y] == '3':
                        return True
                    # visit 안 했으면
                    elif not visited[new_x][new_y]:
                        back = DFS(new_x, new_y)
                        if back: return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    visited = [[False for i in range(N)] for j in range(N)]

    # 미로 생성
    maze = []
    for _ in range(N):
        maze.append(input())
    # 2 시작
    x, y = StartPoint(maze)
    # 1은 방문했다고 치고
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '1':
                visited[i][j] = True

    # 탈출 가능하면 1, 불가능하면 0
    if DFS(x, y):
        ans = 1
    else:
        ans = 0

    print("#{0} {1}".format(tc, ans))
