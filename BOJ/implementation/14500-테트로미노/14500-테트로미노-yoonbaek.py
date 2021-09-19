from sys import stdin
from collections import deque

rd = lambda : map(int, stdin.readline().split())

MOVES = ((0, -1), (0, 1), (-1, 0), (1, 0))

def DFS(start):
    s = deque([start])
    visited[start] = 1
    
    while s:
        now_x, now_y = s.pop()
        for x, y in MOVES:
            moved_x = now_x + x
            moved_y = now_y + y

            if 0 <= moved_x < M and 0 <= moved_y < N:
                if not visited[moved_y][moved_x]:
                    visited[moved_y][moved_x] = visited[now_x][now_y] + 1
                    s.append((moved_x, moved_y))

if __name__ == "__main__":
    N, M = rd()

    paper = [list(rd()) for i in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]


    print(visited)

# git commit -m "code: Solve boj 14500 테트로미노 (yoonbaek)"