from collections import deque
moves = ((0, -1), (0, 1), (-1, 0), (1, 0))

def dijkstra(start):
    q = deque([start])
    costs[start[1]][start[0]] = 0

    while q:
        col, row = q.popleft()
        
        for x, y in moves:
            x += col
            y += row
            if 0 <= x < N and 0 <= y < N:
                diff = heights[y][x] - heights[row][col]
                diff = 1 if diff <= 0 else diff+1
                cost = costs[row][col] + diff

                if costs[y][x] > cost:
                    costs[y][x] = cost
                    q.append((x, y))
                    

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())

        heights = [list(map(int, input().split())) for _ in range(N)]
        costs = [[100000 for _ in range(N)] for _ in range(N)]

        dijkstra((0,0))

        print(f"#{tc} {costs[N-1][N-1]}")
        
# git commit -m "code: Solve swea L5250 최소 비용 (yoonbaek)"