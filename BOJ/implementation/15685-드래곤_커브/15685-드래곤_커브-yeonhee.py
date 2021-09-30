import sys
input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

graph = [[0]*101 for _ in range(101)]

for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1
    moves = [d]

    for _ in range(g):
        moves += ((move+1)%4 for move in moves[::-1])

    for move in moves:
        nx = x + dx[move]
        ny = y + dy[move]
        graph[nx][ny] = 1
        x, y = nx, ny

result = 0

for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            result += 1

print(result)
