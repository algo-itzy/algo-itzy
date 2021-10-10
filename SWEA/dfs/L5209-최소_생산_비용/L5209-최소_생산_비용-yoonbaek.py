def DFS(acc, recur):
    global min_cost

    if acc >= min_cost:
        return

    # 재귀횟수가 N에 도달하면 합격
    if recur == N:
        min_cost = acc
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            DFS(acc+costs[recur][i], recur+1)
            visited[i] = 0
            

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        min_cost = 99*(N**2)+1

        costs = []
        for _ in range(N):
            costs.append(list(map(int, input().split())))

        visited = [0] * N
        
        DFS(0,0)

        print(f"#{tc} {min_cost}")

# git commit -m "code: Solve swea L5209 최소 생산 비용 (yoonbaek)"