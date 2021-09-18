# git commit -m "code: Solve boj 14502 연구소 (seungkyu)"
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
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                for k in range(N):
                    for l in range(M):
                        if matrix[k][l] == 0:
                            for m in range(N):
                                for n in range(M):
                                    if matrix[m][n] == 0:
                                        if (i == k and j == l): continue
                                        if (i == m and j == n): continue
                                        if (k == m and l == n): continue
                                    
                                        matrix[i][j] = 1
                                        matrix[k][l] = 1
                                        matrix[m][n] = 1
                                        cnt = bfs()
                                        ans = max(ans, cnt)
                                        matrix[i][j] = 0
                                        matrix[k][l] = 0
                                        matrix[m][n] = 0   
    return ans


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

print(choose_wall())