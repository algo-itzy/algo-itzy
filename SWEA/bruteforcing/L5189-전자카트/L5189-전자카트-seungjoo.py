# git commit -m "code: Solve swea L5189 전자카트 (seungjoo)"
def dfs(depth, cur_node, total):
    global min_sum
    if depth == N-1:
        min_sum = min(min_sum, total + matrix[cur_node][0])
        return
    if total > min_sum:
        return
    for next_node in range(N):
        if not col_check[next_node]:
            col_check[next_node] = True
            dfs(depth + 1, next_node, total + matrix[cur_node][next_node])
            col_check[next_node] = False


for test in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    col_check = [False] * N
    min_sum = float('inf')
    col_check[0] = True
    dfs(0, 0, 0)
    print(f'#{test} {min_sum}')