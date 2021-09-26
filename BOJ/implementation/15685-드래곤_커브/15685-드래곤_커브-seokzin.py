D = ((1, 0), (0, -1), (-1, 0), (0, 1))

n = int(input())
visit = [[0] * 101 for _ in range(101)]
res = 0

for _ in range(n):
    x, y, d, g = map(int, input().split())
    visit[x][y] = 1
    dir = [d]

    for _ in range(g):
        dir += [(i+1) % 4 for i in dir][::-1]  # 이전 세대에 1씩 더해 뒤집기

    for d in dir:
        x, y = x+D[d][0], y+D[d][1]
        visit[x][y] = 1

for i in range(100):
        for j in range(100):
            if visit[i][j] and visit[i][j+1] and visit[i+1][j] and visit[i+1][j+1]:
                res += 1

print(res)