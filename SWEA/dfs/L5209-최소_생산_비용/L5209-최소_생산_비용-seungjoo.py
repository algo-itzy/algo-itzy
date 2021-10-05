# git commit -m "code: Solve swea L5209 최소 생산 비용 (seungjoo)"
def dfs(depth, total):
    global min_sum
    if depth == N:
        min_sum = min(min_sum, total)
        return
    if total > min_sum:
        return
    for next_node in range(N):
        if not col_check[next_node]:
            col_check[next_node] = True
            dfs(depth + 1, total + matrix[depth][next_node])
            col_check[next_node] = False


for test in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    col_check = [False] * N
    min_sum = float('inf')
    dfs(0, 0)
    print(f'#{test} {min_sum}')