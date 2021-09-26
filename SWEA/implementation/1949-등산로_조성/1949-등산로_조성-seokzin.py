D = ((-1,0), (1,0), (0,-1), (0,1))


def dfs(x, y, step, dig):
    global res

    if step > res:
        res = step

    visit[x][y] = 1

    for dx, dy in D:
        nx, ny = x+dx, y+dy

        if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
            if arr[x][y] > arr[nx][ny]:
                dfs(nx, ny, step+1, dig)
            elif dig and arr[x][y] > arr[nx][ny] - k:  # 높거나 같은 곳 이동시
                tmp = arr[nx][ny]
                arr[nx][ny] = arr[x][y] - 1
                dfs(nx, ny, step+1, 0)
                arr[nx][ny] = tmp  # 복구
        
    visit[x][y] = 0


for tc in range(1, int(input())+1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    h = max(map(max, arr))  # 최대 h로 초기화
    visit = [[0]*n for _ in range(n)]
    res = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == h:
                dfs(i, j, 1, 1)

    print(f"#{tc} {res}")
