# git commit -m "code: Solve swea 1949 등산로 조성 (jiwoong)"
def index(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


def dfs(x, y, cut, road, height):
    global ans
    visited[x][y] = 1
    if road > ans:
        ans = road
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if index(nx, ny) and not visited[nx][ny]:
            if height > info[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, cut, road + 1, info[nx][ny])
                visited[nx][ny] = 0
            elif not cut and height <= info[nx][ny]:
                if info[nx][ny] - K < height:
                    visited[nx][ny] = 1
                    dfs(nx, ny, cut + 1, road + 1, height - 1)
                    visited[nx][ny] = 0


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start = 0
    for i in range(N):
        for j in range(N):
            if info[i][j] >= start:
                start = info[i][j]
    cut = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            if info[i][j] == start:
                visited = [[0] * N for _ in range(N)]
                dfs(i, j, 0, 0, start)
    print('#{} {}'.format(tc, ans + 1))
