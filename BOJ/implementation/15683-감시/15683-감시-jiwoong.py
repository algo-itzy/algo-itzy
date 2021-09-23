# git commit -m "code: Solve boj 15683 감시 (jiwoong)"
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def select(selected, ni, nj, d):
    while 1:
        ni += dx[d]
        nj += dy[d]
        if ni < 0 or ni >= N:
            break
        if nj < 0 or nj >= M:
            break
        if arr[ni][nj] == 6:
            break
        selected[ni][nj] = 1
    return selected


def check(dir):
    global min_cnt
    selected = [[0] * M for _ in range(N)]
    for i in range(len(wall)):
        selected[wall[i][0]][wall[i][1]] = 6
    for i in range(len(dir)):
        ni, nj = cctv[i][1], cctv[i][2]
        selected[ni][nj] = 1
        if cctv[i][0] == 1:
            d = dir[i]
            selected = select(selected, ni, nj, d)
        elif cctv[i][0] == 2:
            if dir[i] == 0 or dir[i] == 2:
                for d in range(0, 3, 2):
                    selected = select(selected, ni, nj, d)
            elif dir[i] == 1 or dir[i] == 3:
                for d in range(1, 4, 2):
                    selected = select(selected, ni, nj, d)
        elif cctv[i][0] == 3:
            if dir[i] == 0:
                for d in range(2):
                    selected = select(selected, ni, nj, d)
            elif dir[i] == 1:
                for d in range(1, 3):
                    selected = select(selected, ni, nj, d)
            elif dir[i] == 2:
                for d in range(2, 4):
                    selected = select(selected, ni, nj, d)
            elif dir[i] == 3:
                for d in range(0, 4, 3):
                    selected = select(selected, ni, nj, d)
        elif cctv[i][0] == 4:
            if dir[i] == 0:
                for d in range(4):
                    if d == 2:
                        continue
                    selected = select(selected, ni, nj, d)
            elif dir[i] == 1:
                for d in range(4):
                    if d == 3:
                        continue
                    selected = select(selected, ni, nj, d)
            elif dir[i] == 2:
                for d in range(4):
                    if d == 0:
                        continue
                    selected = select(selected, ni, nj, d)
            elif dir[i] == 3:
                for d in range(4):
                    if d == 1:
                        continue
                    selected = select(selected, ni, nj, d)
        elif cctv[i][0] == 5:
            for d in range(4):
                selected = select(selected, ni, nj, d)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if selected[i][j] == 0:
                cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
    return


def get_ans(idx, dir):
    global min_cnt
    if min_cnt == 0:
        return
    if idx == len(dir):
        check(dir)
        return
    for i in range(4):
        if dir[idx] == 5:
            get_ans(idx + 1, dir)
            break
        dir[idx] = i
        get_ans(idx + 1, dir)


N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
cctv = []
wall = []
min_cnt = N * M
for n in range(N):
    for m in range(M):
        if 1 <= arr[n][m] <= 5:
            cctv.append([arr[n][m], n, m])
        elif arr[n][m] == 6:
            wall.append([n, m])

dir = [0] * len(cctv)
for i in range(len(cctv)):
    if cctv[i][0] == 5:
        dir[i] = 5
get_ans(0, dir)
print(min_cnt)
