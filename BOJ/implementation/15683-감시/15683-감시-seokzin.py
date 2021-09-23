from copy import deepcopy
import sys

input = sys.stdin.readline

DIR = ((1,0), (-1,0), (0,1), (0,-1))
CCTV = [[], [[0], [1], [2], [3]], [[0,1], [2,3]], [[3,0], [0,2], [2,1], [1,3]], 
[[1,3,0], [3,0,2], [0,2,1], [2,1,3]], [[0,1,2,3]]]


def fill(x, y, arr, D):
    for i in D:
        nx, ny = x, y
        
        while True:
            nx += DIR[i][0]
            ny += DIR[i][1]

            if 0 <= nx < m and 0 <= ny < n:
                if arr[ny][nx] == 6:
                    break
                elif arr[ny][nx] == 0:
                    arr[ny][nx] = "#"
            else:
                break


def dfs(arr, step):
    global res

    cpy = [row[:] for row in arr]

    if step == len(cctv):
        cnt = 0

        for i in range(n):
            cnt += cpy[i].count(0)

        res = min(res, cnt)

        return

    x, y, idx = cctv[step]

    for D in CCTV[idx]:
        fill(x, y, cpy, D)
        dfs(cpy, step+1)
        cpy = [row[:] for row in arr]


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []
res = sys.maxsize

for i in range(m):
    for j in range(n):
        if arr[j][i] in range(1, 6):
            cctv.append([i, j, arr[j][i]])

dfs(arr, 0)
print(res)