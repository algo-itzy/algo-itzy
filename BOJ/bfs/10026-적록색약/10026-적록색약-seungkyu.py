import sys
from collections import deque

DIRECTION = ((-1, 0), (1, 0), (0, 1), (0, -1))

def bfs(start):
    x, y = start
    queue.append(start)
    color = image[x][y]  # 시작점 color

    while queue:
        x, y = queue.popleft()

        # 적록색양 bfs 다시 돌리기 위해서 모든 G를 R로 변환
        if color == 'G':
            image[x][y] = 'R'

        for i in range(4):
            new_x = x + DIRECTION[i][0]
            new_y = y + DIRECTION[i][1]

            if 0<=new_x<N and 0<=new_y<N:
                if image[new_x][new_y] == color and not visited[new_x][new_y]:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = 1
    

input = sys.stdin.readline
N = int(input())
image = [list(map(str, input().strip())) for _ in range(N)]
queue = deque()


# 정상
visited = [[0]*N for _ in range(N)]
ans1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ans1 += 1
            bfs((i, j))


# 적록색약
visited = [[0]*N for _ in range(N)]
ans2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ans2 += 1
            bfs((i, j))

print(ans1, ans2, sep=' ')

# git commit -m "code: Solve boj 10026 적록색약 (seungkyu)"