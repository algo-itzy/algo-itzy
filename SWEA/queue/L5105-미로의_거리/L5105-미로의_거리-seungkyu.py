import sys
from collections import deque

sys.stdin = open('input.txt')

def mase():  # bfs
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0<=next_x<N and 0<=next_y<N:  # 범위를 벗어나지 않았을 때 0인지 3인지 검사
                # 방문하지 않은 점 거리 = 0
                if matrix[next_x][next_y] == 0 and not dist[next_x][next_y]:
                    queue.append([next_x, next_y])
                    dist[next_x][next_y] = dist[x][y] + 1  # 거리 그 전 점 +1
                elif matrix[next_x][next_y] == 3:
                    return dist[x][y]
    else:  # 길 없을 때
        return 0
        
T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    dist = [[0]*N for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                x = i
                y = j
                break
    queue = deque()
    queue.append([x, y])
    
    print(f'#{test_case} {mase()}')