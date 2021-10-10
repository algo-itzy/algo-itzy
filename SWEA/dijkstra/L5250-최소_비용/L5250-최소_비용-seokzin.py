from collections import deque

D = ((1, 0), (0, 1), (-1, 0), (0, -1))

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    dist[0][0] = 0
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for dy, dx in D:
            nx, ny = x+dx, y+dy

            if 0 <= ny < n and 0 <= nx < n:
                fuel = 1 + max(arr[ny][nx] - arr[y][x], 0)  # 낮은 언덕 이동시 연료 0 보정

                if dist[ny][nx] > dist[y][x] + fuel:
                    dist[ny][nx] = dist[y][x] + fuel
                    q.append((nx, ny))

    print(f'#{tc}', dist[-1][-1])