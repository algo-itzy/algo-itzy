# git commit -m "code: Solve boj 15685 드래곤 커브 (seungkyu)"
import sys
input = sys.stdin.readline
DIRS = ((1, 0),(0, -1),(-1, 0),(0, 1))


def check(x, y):
    for i in range(x, x+2):
        for j in range(y, y+2):
            if mat[i][j] == 0:
                return False
    return True
        

def dragon(mat, dirs, x, y):
    mat[x][y] = 1
    for _ in range(g):
        dirs += [(i+1) % 4 for i in dirs[::-1]]
    for dir in dirs:
        x += DIRS[dir][0]
        y += DIRS[dir][1]
        mat[x][y] = 1


mat = [[0]*101 for _ in range(101)]
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dirs = [d]
    dragon(mat, dirs, x, y)

cnt = 0
for i in range(100):
    for j in range(100):
        if check(i, j):
            cnt += 1
print(cnt)
