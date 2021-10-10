# git commit -m "code: Solve swea L5250 최소 비용 (jiwoong)"
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global ans
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                new = 1  
                if H[nx][ny] > H[x][y]:
                    new += H[nx][ny] - H[x][y]
                if ans[nx][ny] > ans[x][y] + new:
                    ans[nx][ny] = ans[x][y] + new 
                    q.append((nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    ans = [[float('inf') for _ in range(N)] for _ in range(N)]
    ans[0][0] = 0
    bfs(0, 0) 

    print("#{} {}".format(tc, ans[N - 1][N - 1]))
