import copy
import sys

input = sys.stdin.readline


def virus(s, cnt):
    global ans
    if cnt == 3:
        new_arr = copy.deepcopy(arr)
        for k in range(len(virus_list)):
            x, y = virus_list[k]
            bfs(x, y, new_arr)
        cnt = sum(a.count(0) for a in new_arr)
        ans = max(ans, cnt)
        return
    else:
        for i in range(s, N * M):
            x = i // M
            y = i % M
            if arr[x][y] == 0:
                arr[x][y] = 1
                virus(i, cnt + 1)
                arr[x][y] = 0


def bfs(x, y, new_arr):
    if new_arr[x][y] == 2:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                new_arr[nx][ny] = 2
                bfs(nx, ny, new_arr)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
virus_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus_list.append([i, j])

virus(0, 0)
print(ans)
