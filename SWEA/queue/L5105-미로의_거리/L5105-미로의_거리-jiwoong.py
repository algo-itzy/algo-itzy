def bfs(x, y, z, visited):
    # 상하좌우
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # 현재 위치 queue
    q = [(x, y, z)]
    # 큐가 빌 때까지
    while q:
        curr_x, curr_y, curr_z = q.pop(0)
        visited[curr_y][curr_x] = 1
        for i in range(4):
            # 나가지 않으면
            if 0 <= curr_y + dy[i] < N and 0 <= curr_x + dx[i] < N:
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                if arr[new_y][new_x] == 3:
                    return curr_z
                if not arr[new_y][new_x] and not visited[new_y][new_x]:
                    q.append((new_x, new_y, curr_z + 1))
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input())))
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                print(f'#{tc} {bfs(j, i, 0, visited)}')
