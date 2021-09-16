from collections import deque


def bfs(x, y):
    D = ((-1,0), (0,-1), (0,1), (1,0))

    q = deque([(x, y)])
    visit = [[0] * n for _ in range(n)]

    time = 0
    shark = 2  # 현재 아기 상어의 크기다.
    eat = 0
    eat_flag = False  # 현재 상태에서 물고기를 먹은 경우, 
                      # for _ in range(size) 구문을 진행하지 않기 위한 플래그다.
    answer = 0

    while q:
        q = deque(sorted(q))  # 이거 없앨 수 없을까

        for _ in range(len(q)):
            x, y = q.popleft()

            if arr[x][y] and arr[x][y] < shark:  # 작은 물고기 먹음
                arr[x][y] = 0
                eat += 1

                if eat == shark:  # 크기만큼 먹으면 진화
                    shark += 1
                    eat = 0               

                q = deque([(x, y)])  # 먹고난 뒤 다시 BFS 시작
                visit = [[0]*n for _ in range(n)]
                eat_flag = True

                # 먹었을 때의 시간을 저장해둔다.
                answer = time

            for dx, dy in D:
                nx, ny = x+dx, y+dy

                if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                    if arr[nx][ny] <= shark:
                        q.append((nx, ny))
                        visit[nx][ny] = 1

            # 현재 위치에서 먹었다면, 더 이상 위 반복문을 돌 필요가 없다.
            if eat_flag:
                eat_flag = False
                break

        time += 1
    return answer


n = int(input())
arr = [list(map(int , input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            print(bfs(i, j))

# 너무 오래 걸리는 것 같아서 보류. 다시 리팩토링 함

# git commit -m "code: Solve boj 16236 아기 상어 (seokzin)"