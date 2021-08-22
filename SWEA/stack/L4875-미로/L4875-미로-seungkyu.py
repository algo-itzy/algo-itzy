import sys
from collections import deque
sys.stdin = open('sample2.txt')

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
                if matrix[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    queue.append([next_x, next_y])
                    visited[next_x][next_y] = 1  # 방문 표시
                elif matrix[next_x][next_y] == 3:
                    return 1
    else:  # 길 없을 때
        return 0


T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                x = i
                y = j
                break
    visited = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append([x, y])
    
    print(f'#{test_case} {mase()}')
    
'''
dfs로 풀었다가 시간초과 났습니다
'''
# def mase(x, y):  # DFS
#     global ans  # 답 저장
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
    
#     visited.append([x, y])  # x, y점 방문 표시
#     for i in range(4):
#         next_x = x + dx[i]
#         next_y = y + dy[i]

#         if 0<=next_x<N and 0<=next_y<N:  # 범위를 벗어나지 않았을 때 0인지 3인지 검사
#             if matrix[next_x][next_y] == 0 and [next_x, next_y] not in visited:
#                 mase(next_x, next_y)
#             elif matrix[next_x][next_y] == 3:
#                 ans = 1
#                 return