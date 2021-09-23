import sys
input = sys.stdin.readline

delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [1, 3], [2, 1], [3, 0]],
    [[0, 2, 1], [1, 3, 0], [2, 1, 3], [3, 0, 2]],
    [[0, 1, 2, 3]],
]


def get_blind_spots(graph):
    cnt = 0
    for r in range(n):
        for c in range(m):
            if not graph[r][c]:
                cnt += 1
    return cnt


def dfs(graph, idx):
    global result
    tmp = [[i for i in row] for row in graph]

    if idx == cctv_cnt:
        result = min(result, get_blind_spots(tmp))
        return

    r, c, cctv_type = cctv[idx]
    for dirs in directions[cctv_type]:
        for d in dirs:
            dr, dc = delta[d]
            nr, nc = r, c
            while True:
                nr += dr
                nc += dc
                if 0 <= nr < n and 0 <= nc < m and tmp[nr][nc] != 6:
                    if not tmp[nr][nc]:
                        tmp[nr][nc] = '#'
                else:
                    break
        dfs(tmp, idx+1)
        tmp = [[i for i in row] for row in graph]


n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []
cctv_cnt = 0

for r in range(n):
    for c in range(m):
        if 0 < office[r][c] < 6:
            cctv.append((r, c, office[r][c]))
            cctv_cnt += 1

result = n*m
dfs(office, 0)
print(result)
