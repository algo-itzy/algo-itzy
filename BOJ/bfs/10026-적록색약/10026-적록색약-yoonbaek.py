from sys import stdin
from collections import deque

rd = stdin.read

MOVES = ((0, -1), (0, 1), (1, 0), (-1, 0))

# R/G/B
def BFS_tri(start):
    q = deque([start])
    visited[start[1]][start[0]] = 2 if grid[start[1]][start[0]] == "B" else 1

    while q:
        now = q.popleft()

        for move in MOVES:
            next_x = now[0]+move[0]
            next_y = now[1]+move[1]
            if 0 <= next_x < N and 0 <=next_y < N:
                next = grid[next_y][next_x]
                if next == grid[now[1]][now[0]]:
                    if not visited[next_y][next_x]:
                        visited[next_y][next_x] = 2 if next == "B" else 1
                        q.append((next_x, next_y))

# RG/B
def BFS_bi(start):
    q = deque([start])
    s = visited[start[1]][start[0]]
    visited[start[1]][start[0]] = 0

    while q:
        now = q.popleft()

        for move in MOVES:
            next_x = now[0] + move[0]
            next_y = now[1] + move[1]
            if 0 <= next_x < N and 0 <=next_y < N:
                next = visited[next_y][next_x]
                if next and next == s:
                    visited[next_y][next_x] = 0
                    q.append((next_x, next_y))
        

if __name__ == "__main__":
    inputs = rd().split()
    N = int(inputs[0])
    grid = inputs[1:]
    visited = [[0 for i in range(N)] for i in range(N)]
    cnt1, cnt2 = 0, 0

    # BFS 돌면서 visited를 1과 2, 두가지 색으로 바꿔줍니다.
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS_tri((j,i))
                cnt1 += 1

    # 1과 2, 두가지로 바꾼 visited를 기준으로 BFS를 다시 순회합니다.
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                BFS_bi((j,i))
                cnt2 += 1
                
    print(cnt1, cnt2)

# git commit -m "code: Solve boj 10026 적록색약 (yoonbaek)"