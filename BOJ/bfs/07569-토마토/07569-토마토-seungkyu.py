from collections import deque
import sys
# 토마토 4방향 이동 문제와 매우 유사

def bfs():
    # 6방향 이동..
    dy = [1, -1, 0, 0, 0, 0]
    dx = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            new_x = x + dx[i]
            new_y = y + dy[i]
            new_z = z + dz[i]
            # 이동한 곳이 범위를 벗어나지 않고, 익지않은 토마토일때
            if 0<=new_x<H and 0<=new_y<N and 0<=new_z<M and matrix[new_x][new_y][new_z] == 0:
                matrix[new_x][new_y][new_z] = matrix[x][y][z] + 1
                queue.append((new_x, new_y, new_z))


def check():
    ans = 0
    for i in matrix:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    return
            ans = max(ans, max(j))
    print(ans-1)

queue = deque()
input = sys.stdin.readline
M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                queue.append((i, j, k))
bfs()
check()

# git commit -m "code: Solve boj 07569 토마토 (seungkyu)"