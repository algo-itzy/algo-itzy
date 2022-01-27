# git commit -m "code: Solve boj 21610 마법사 상어와 비바라기 (seungkyu)"
from collections import deque
import sys
input = sys.stdin.readline

delta = ((0, -1),(-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1))
diagonal = ((-1, -1), (1, -1), (-1, 1), (1, 1))

def cal_water(board):
    tot = 0
    for row in board:
        tot += sum(row)
    return tot

def find_clouds(board, cmds):
    for i in range(M):
        if i == 0:
            clouds = [[N-1, 0],[N-1, 1],[N-2, 0],[N-2, 1]]
            new_clouds = move_clouds(cmds[i], clouds)
        else:
            clouds = []
            for j in range(N):
                for k in range(N):
                    if board[j][k] >= 2 and (j, k) not in new_clouds:
                        board[j][k] -= 2
                        clouds.append([j, k])
            new_clouds = move_clouds(cmds[i], clouds)
        
        add_water(board, new_clouds)

    for j in range(N):
        for k in range(N):
            if board[j][k] >= 2 and (j, k) not in new_clouds:
                board[j][k] -= 2


def move_clouds(cmd, clouds):
    new_clouds = set()
    d, s = cmd
    for cloud in clouds:
        x, y = cloud
        nx = (N+x+delta[d-1][0]*s) % N
        ny = (N+y+delta[d-1][1]*s) % N
        new_clouds.add((nx, ny))

    return new_clouds


def add_water(board, clouds):
    for cloud in clouds:
        x, y = cloud
        board[x][y] += 1

    for cloud in clouds:
        check_diag_water(board, cloud)
    

def check_diag_water(board, cloud):
    x, y = cloud
    cnt = 0
    for dx, dy in diagonal:
        nx = x + dx
        ny = y + dy

        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny]:
                cnt += 1

    board[x][y] += cnt  # 물복사


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmds = []
for _ in range(M):
    d, s = map(int, input().split())
    cmds.append([d, s])
    
find_clouds(board, cmds)
print(cal_water(board))