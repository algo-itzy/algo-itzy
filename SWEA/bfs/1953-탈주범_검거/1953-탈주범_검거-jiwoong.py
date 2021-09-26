# git commit -m "code: Solve swea 1953 탈주범 검거 (jiwoong)"
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
pipe = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]


def check(time):
    if time >= L:
        return
    for _ in range(len(q)):
        pos = q.pop(0)
        r = pos[0]
        c = pos[1]
        for i in pipe[info[r][c]]:
            nr = r + dxy[i][0]
            nc = c + dxy[i][1]
            if 0 <= nr <= N - 1 and 0 <= nc <= M - 1 and (i + 2) % 4 in pipe[info[nr][nc]] and (nr, nc) not in visited:
                q.append((nr, nc))
                visited.append((nr, nc))
    time += 1
    check(time)


for t in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    q = [(R, C)]
    visited = [(R, C)]
    check(1)
    print("#%d %d" % (t, len(visited)))
