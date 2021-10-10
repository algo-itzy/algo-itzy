from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                diff = 0                                # 같은 높이 혹은 더 낮은 곳으로 이동하는 경우
                if arr[nx][ny] - arr[x][y] > 0:         # 더 높은 곳으로 이동하는 경우
                    diff = arr[nx][ny] - arr[x][y]      # 차이만큼 추가로 연료

                if visited[nx][ny] > visited[x][y] + diff + 1: # 이동하는 곳의 비용이 큰 경우, 작은 것으로 업뎃해줘야 하기에
                    visited[nx][ny] = visited[x][y] + diff + 1
                    queue.append((nx, ny))

    return


t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)] # 각 칸의 높이 값을 받음
    visited = [[float('inf')] * n for _ in range(n)]          # 각 칸의 값을 무한대로 초기 설정
    visited[0][0] = 0

    bfs(0, 0)                                                 # 시작 좌표
    print(f'#{tc+1} {visited[-1][-1]}')                       # 맨 오른쪽 아래의 좌표 값을 출력

# git commit -m "code: Solve swea L5250 최소 비용 (yeonju)"