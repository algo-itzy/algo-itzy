from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    cnt = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 0
            res.append(bfs(i, j))
res.sort()
print(len(res))
for n in res:
    print(n)

# git commit -m "code: Solve boj 02667 단지번호붙이기 (yeonju)"
