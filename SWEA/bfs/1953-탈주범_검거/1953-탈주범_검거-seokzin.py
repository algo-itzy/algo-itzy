D = ((1,0), (0,1), (-1,0), (0,-1))  # 동남서북

PIPE = [
    [],
    [0, 1, 2, 3],
    [1, 3],
    [0, 2],
    [0, 3],
    [0, 1],
    [1, 2],
    [2, 3]
]

for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    res = 0


    q = [(c, r)]
    visit[r][c] = 1

    while q:
        x, y = q.pop(0)
        res += 1

        if visit[y][x] >= l:
            continue

        for i in PIPE[arr[y][x]]:
            nx, ny = x+D[i][0], y+D[i][1]

            if 0<=nx<m and 0<=ny<n and arr[ny][nx] and not visit[ny][nx]:
                if (i+2)%4 in PIPE[arr[ny][nx]]:  # 다음 파이프가 연결돼있다면
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((nx, ny))

    print(f"#{tc}", res)

# 36) 다음 파이프 연결 체크가 핵심 로직