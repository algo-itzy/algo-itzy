from collections import deque


def bfs():
    D = ((1,0,0), (0,1,0), (-1,0,0), (0,-1,0), (0,0,-1), (0,0,1))
    q = deque()

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if arr[z][x][y] == 1:
                    q.append([z, x, y])

    while q:
        z, x, y = q.popleft()

        for dx, dy, dz in D:
            nx, ny, nz = x+dx, y+dy, z+dz
            
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and not arr[nz][nx][ny]:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                q.append([nz, nx, ny])


def count():  # 굳이 함수화 한 이유는 flag 쓰기 싫어서
    res = 0

    for floor in arr:
        for row in floor:
            for x in row:
                if x == 0:
                    return -1
                else:
                    res = max(res, x-1)

    return res


m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

bfs()

print(count())

# 최대값 찾기에 map을 2번 도입했는데 여기서 오류가 생겼습니다.. 엄청 해맸음
# res = max(map(max, map(max, arr))) - 1