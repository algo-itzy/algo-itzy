import sys
sys.stdin = open('input.txt')

def mase(x, y):  # DFS
    global ans  # 답 저장
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited[x][y] = 1  # 방문 표시
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0<=next_x<N and 0<=next_y<N:  # 범위 벗어나지 않을 때 0인지 3인지
            if matrix[next_x][next_y] == 0 and not visited[next_x][next_y]:
                mase(next_x, next_y)
                
            elif matrix[next_x][next_y] == 3:
                ans = 1
                return

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
    visited = [[0]*N for _ in range(N)]  # 방문 표시 리스트
    ans = 0
    mase(x, y)
    print(f'#{test_case} {ans}')
    