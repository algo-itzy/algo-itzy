# git commit -m "code: Solve swea L5188 최소합 (jiwoong)"
dx = [0, 1]
dy = [1, 0]


def dfs(x, y):
    global ans, arr
    if ans < arr:  # 현재 결과값 보다 크면 함수 끝나도록 -> 제한시간때문에 가지치기 해야함
        return
    if x == N - 1 and y == N - 1:
        ans = arr
        return
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if (nx, ny) not in visited:
            visited.append((nx, ny))  # 좌표 업로드
            arr += nums[nx][ny]
            dfs(nx, ny)
            arr -= nums[nx][ny]  # 원상복구
            visited.remove((nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    ans = 3000
    arr = nums[0][0]
    dfs(0, 0)  # 현재좌표
    print("#{} {}".format(tc, ans))
