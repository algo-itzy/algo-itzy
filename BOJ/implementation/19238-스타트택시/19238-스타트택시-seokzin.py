import sys
from collections import deque
from heapq import heappop, heappush

input = sys.stdin.readline


def bfs():
    global f

    D = ((1,0), (-1,0), (0,1), (0,-1))

    sy, sx = pos[0]-1, pos[1]-1
    check = [[0] * n for _ in range(n)]
    table = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    q = deque([])
    table[sy][sx] = 0
    q.append([sy, sx])
    check[sy][sx] = True
    
    while q:
        y, x = q.popleft()

        for dx, dy in D:
            nx, ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < n:
                if not check[ny][nx]:
                    check[ny][nx] = 1
                    if arr[ny][nx] != 1:
                        table[ny][nx] = table[y][x] + 1
                        q.append([ny, nx])
    
    return table


def find():  # 가까운 손님 찾기
    global f

    table = bfs()
    hq = []

    for i in range(m):
        if not visit[i]:
            y, x = data[i][0]-1, data[i][1]-1
            d = table[y][x]

            if f >= d:
                heappush(hq, (d, y, x, i))  # 탑승객 우선순위 보장

    if not hq: 
        return -1

    d, _, _, idx = heappop(hq)
    f -= d
    visit[idx] = 1

    return idx


def go(idx):  # 목적지 이동
    global f

    table = bfs()

    y, x = data[idx][2]-1, data[idx][3]-1
    d = table[y][x]

    if f < d: 
        return -1

    return d


n, m, f = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pos = list(map(int, input().split()))  # 택시 좌표
data = [list(map(int, input().split())) for _ in range(m)]
visit = [0] * m


for _ in range(m):
    idx = find()

    if idx == -1:
        print(-1)
        break

    pos = data[idx][0], data[idx][1]

    d = go(idx)

    if d == -1:
        print(-1)
        break

    f += d

    pos = data[idx][2], data[idx][3]
else:
    print(f)

# 지속적 리팩토링 필요..