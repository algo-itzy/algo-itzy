def solution(product, cost):
    global min_value
    if product == n: # 다 했으면
        min_value = min(cost, min_value)
        return

    if cost > min_value: # 현재까지의 비용이 이미 최소비용을 넘으면 무시
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            solution(product + 1, cost + table[product][i])
            visited[i] = 0


for tc in range(int(input())):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    visited = [0] * n

    min_value = 10000000
    solution(0, 0)
    print(f'#{tc+1} {min_value}')

# git commit -m "code: Solve swea L5209 최소 생산 비용 (yeonju)"