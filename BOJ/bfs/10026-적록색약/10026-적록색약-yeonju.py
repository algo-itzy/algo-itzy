# 적록색약: red = green
from collections import deque

n = int(input())
pic = [list((input())) for i in range(n)]

njuk_cnt, juk_cnt = 0, 0 # 적록색약과 적록색약이 아닌 사람이 볼 구역의 개수를 카운트하는 변수

dx= [1, -1, 0, 0]
dy= [0, 0, 1, -1]

queue = deque()
c = [[0]*n for _ in range(n)]

def bfs(x, y):
    queue.append((x, y))
    c[x][y]= 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if pic[nx][ny] == pic[x][y] and c[nx][ny] == 0:
                    queue.append((nx, ny))
                    c[nx][ny] = 1


for i in range(n):              # 적록색약이 아닌 사람 먼저
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j)
            njuk_cnt += 1

for i in range(n):              # 적록색약인 경우
    for j in range(n):          # Red 를 Green 으로 바꿔주기
        if pic[i][j] == 'R':
            pic[i][j] = 'G'

queue = deque()
c = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j)
            juk_cnt += 1

print(njuk_cnt, juk_cnt)



# git commit -m "code: Solve boj 10026 적록색약 (yeonju)"