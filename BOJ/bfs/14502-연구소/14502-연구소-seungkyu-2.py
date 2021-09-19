# git commit -m "code: Solve boj 14502 연구소 (seungkyu)"
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
'''
pypy로 제출했습니다.
'''
DIRS = ((1,0),(-1,0),(0,1),(0,-1))

def bfs():
    visited = [[0]*M for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                q.append((i,j))
                visited[i][j] = 2
    while q:
        x, y = q.popleft()

        for dir_x, dir_y in DIRS:
            next_x = x + dir_x
            next_y = y + dir_y

            if 0<=next_x<N and 0<=next_y<M:
                if matrix[next_x][next_y] != 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = 2
                    q.append((next_x, next_y))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 1 and visited[i][j] != 2:
                cnt += 1

    return cnt

def choose_wall():
    ans = 0
    candidates = []
    for i in range(N):
        for j in range(M):
            if not matrix[i][j]:  # 0
                candidates.append((i,j))
                walls_comb = combinations(candidates, 3)
                for walls in walls_comb:
                    for wall in walls:
                        i, j = wall
                        matrix[i][j] = 1
                    cnt = bfs()
                    for wall in walls:
                        i, j = wall
                        matrix[i][j] = 0
                    ans = max(ans, cnt)
    return ans


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

print(choose_wall())
