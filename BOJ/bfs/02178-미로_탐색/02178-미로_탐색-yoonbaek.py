from sys import stdin
from collections import deque

# first-class function
ints = lambda x : list(map(int, x))

# move_directions
MOVES = ((0, -1), (0, 1), (-1, 0), (1, 0))

# functions
def search(start):
    moves = []
    for x, y in MOVES:
        next_x, next_y = start[0]+x, start[1]+y
        if 0 <= next_x < M and 0 <= next_y < N:
            if maze[next_y][next_x] == 1:
                moves.append((next_x, next_y))

    return moves
                

def BFS(start):
    q = deque([start])

    while q:
        now = q.popleft()

        moves = search(now)
        for x, y in moves:
            if maze[y][x] == 1:
                # 최초점부터 끝점까지의 거리를 메모
                maze[y][x] = maze[now[1]][now[0]]+1
                q.append((x, y))


if __name__ == "__main__":
    N, M = ints(input().split())

    maze = [ints(input()) for _ in range(N)]

    BFS((0,0))
    # 끝점의 거리를 출력
    print(maze[N-1][M-1])


# git commit -m "code: Solve boj 02178 미로 탐색 (yoonbaek)"