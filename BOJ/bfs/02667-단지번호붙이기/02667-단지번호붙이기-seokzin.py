from collections import deque


def bfs(a, b):
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    q = deque()
    q.append((a, b))
    arr[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for d in D:
            nx, ny = x+d[0], y+d[1]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
                arr[nx][ny] = 0
                cnt += 1
                q.append([nx, ny])

    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            res.append(bfs(i, j))

print(len(res), *sorted(res), sep='\n')

# n=1 일 때 예외 처리에서 해맸음
