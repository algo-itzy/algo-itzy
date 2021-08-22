from collections import deque

def bfs():
    q = deque()
    
    for x in range(N): # 시작지점 탐색
        for y in range(N):
            if arr[y][x] == 2:
                q.append((x, y))
                arr[y][x] = 1

    while q:
        x, y = q.popleft()

        arr[y][x] = 1

        for d in D:
            nx, ny = x+d[0], y+d[1]

            if 0 <= nx < N and 0 <= ny < N and (arr[ny][nx] == 0 or arr[ny][nx] == 3):
                q.append((nx, ny))

                if arr[ny][nx] == 3:
                    return 1

    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))

    print(f'#{tc}', bfs())

# visit를 넣고 풀어봤는데 arr랑 행동이 겹쳐서 그냥 없앴습니다.
# 3에도 이동이 가능하기에 if 검증문이 지저분해졌습니다. 이게 최선일까..