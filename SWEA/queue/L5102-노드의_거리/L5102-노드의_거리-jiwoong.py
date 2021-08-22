def bfs(arr, start, end, visited):
    q = []
    q.append((start, end))
    while q:
        cv, cd = q.pop(0)
        visited[cv] = 1
        for i in range(V + 1):
            if arr[cv][i] and not visited[i]:
                if i == G:
                    return cd + 1
                q.append((i, cd + 1))
    return 0


T = int(input())
for tc in range(1, T + 1):

    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for n in range(E):
        l, r = map(int, input().split())
        arr[l][r] = 1
        arr[r][l] = 1

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(arr, S, 0, visited)}')
