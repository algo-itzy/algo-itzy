# git commit -m "code: Solve swea L5188 최소합 (seungjoo)"
def dfs(x, y, total):
    global min_sum
    if total > min_sum:
        return
    if x == N - 1 and y == N - 1:
        min_sum = min(min_sum, total)
        return
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if nx < N and ny < N:
            dfs(nx, ny, total + matrix[nx][ny])


for test in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    delta = ((1, 0), (0, 1))
    min_sum = float('inf')
    # 총 2N - 1 칸.
    dfs(0, 0, matrix[0][0])
    print(f'#{test} {min_sum}')