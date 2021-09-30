# 아래, 오른 이동 가능
dx = [1, 0]
dy = [0, 1]


def road(x, y, total):

    global ans
    if x == n-1 and y == n-1:       # 도착점에 도달하게 되면
        total += arr[x][y]
        if total < ans:             # 최소값이 더 작다면, 갱신해주기
            ans = total
            return

    if total > ans:                 # ans 보다 여태까지 나온 total이 더 크면, 볼 필요가 없음
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            road(nx, ny, total + arr[x][y])


t = int(input())

for tc in range(t):
    n = int(input())                # 가로 세로 칸 수
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    ans = 10 * n
    road(0, 0, 0)

    print(f'#{tc+1} {ans}')

# git commit -m "code: Solve swea L5188 최소합 (yeonju)"