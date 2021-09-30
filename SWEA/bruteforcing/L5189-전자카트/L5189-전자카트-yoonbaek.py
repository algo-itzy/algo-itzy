def DFS(start, acc, recur):
    global _min

    if acc > _min:
        return

    if recur == N:
        acc += mat[start][0]
        _min = _min if _min < acc else acc
        return

    for next in range(N):
        if not visited[next]:
            if start != next:
                visited[next] = 1
                DFS(next, acc+mat[start][next], recur+1)
                visited[next] = 0


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        
        mat = [list(map(int, input().split())) for _ in range(N)]
        visited = [0 for _ in range(N)]
        visited[0] = 1
        _min = 10000

        DFS(0, 0, 1)
                    
        print(f"#{tc} {_min}")    

# git commit -m "code: Solve swea L5189 전자카트 (yoonbaek)"