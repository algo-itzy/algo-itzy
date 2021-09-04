import sys
from collections import deque

read = sys.stdin.read

MOVES = ((-1, 0), (1, 0), (0, -1), (0, 1))

def search(start):
    moves = []
    for x, y in MOVES:
        next_x, next_y = start[0]+x, start[1]+y
        if 0 <= next_x < N and 0 <= next_y < N:
            if 지도[next_y][next_x] == 1:
                moves.append((next_x, next_y))

    return moves

def BFS(start):
    q = deque([start])
    # check visited
    지도[start[1]][start[0]] = 0
    단지수 = 0

    while q:
        now_x, now_y = q.popleft()
        단지수 += 1
        
        moves = search((now_x, now_y))
        for next_x, next_y in moves:
            if 지도[next_y][next_x]:
                지도[next_y][next_x] = 0
                q.append((next_x, next_y))

    return 단지수

if __name__ == "__main__":
    rd = read().split()
    
    N = int(rd[0])
    지도 = [list(map(int, r)) for r in rd[1:]]

    단지수들 = []

    for 행 in range(N):
        for 열 in range(N):
            if 지도[행][열]:
                단지수들.append(BFS((열, 행)))
    
    단지수들.sort()

    print(len(단지수들))
    print("\n".join(map(str, 단지수들)))
                

# git commit -m "code: Solve boj 02667 단지번호붙이기 (yoonbaek)"