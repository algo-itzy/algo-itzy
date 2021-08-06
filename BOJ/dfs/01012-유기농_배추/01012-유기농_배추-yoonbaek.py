# solved by YoonBaek
# Solved in bfs algorithm
from sys import stdin, stdout
from collections import deque

input = stdin.readline
print = stdout.write

q = deque()
# up-down-left-right
directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

# check near baechus visited
def BFS(x: int, y: int)->None:
    q.append([x, y])

    while q:
        x_now, y_now = q.popleft()

        # walk around four directions
        for x_move, y_move in directions:
            x_moved = x_now + x_move
            y_moved = y_now + y_move

            # if moved place occurs no index error,
            if 0 <= x_moved < col and 0 <= y_moved < row:
                # if it is unvisited baechu,
                if bat[y_moved][x_moved]:
                    # convert to visited baechu
                    bat[y_moved][x_moved] = 0
                    q.append([x_moved, y_moved])


def get_baechu_loc()->None:
    x, y = map(int, input().split())
    bat[y][x] = 1


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        cnt = 0
        col, row, k = map(int, input().split())
        
        # 밭 init
        bat = [[0]*col for _ in range(row)]
        for _ in range(k):
            get_baechu_loc()

        for y in range(row):
            for x in range(col):
                if bat[y][x]:
                    # check visited process
                    bat[y][x] = 0
                    BFS(x, y)
                    cnt+=1

        print(f"{cnt}\n")