from collections import deque

def bfs():
    q = deque()
    
    for x in range(N): # 시작지점 탐색
        for y in range(N):
            if arr[y][x] == 2:
                q.append((x, y, 0))  
                arr[y][x] = 1

    while q:
        x, y, dis = q.popleft()

        arr[y][x] = 1

        for d in D:
            nx, ny = x+d[0], y+d[1]

            if 0 <= nx < N and 0 <= ny < N and (arr[ny][nx] == 0 or arr[ny][nx] == 3):
                if arr[ny][nx] == 3:
                    return dis  # 탈출부

                q.append((nx, ny, dis+1))

    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))

    print(f'#{tc}', bfs())

# 4875 문제의 queue에 dis를 함께 전달했습니다.