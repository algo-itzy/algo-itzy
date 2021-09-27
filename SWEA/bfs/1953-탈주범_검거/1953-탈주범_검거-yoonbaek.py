from collections import deque

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)

pipe_dict = {
    1: (up, down, left, right),
    2: (up, down), 3: (left, right),
    4: (up, right), 5: (down, right), 
    6: (down, left), 7: (up, left)
}

connections = {
    up: down, down:up, left:right, right:left
}

def BFS(start):
    q = deque([start])
    possibles = 1
    visited[start[1]][start[0]] = 1

    while q:
        c, r = q.popleft()

        for x, y in pipe_dict[tunnel[r][c]]:
            con = (x, y)
            x += c; y += r
            if 0 <= x < M and 0 <= y < N:
                if not visited[y][x] and tunnel[y][x]:
                    if connections[con] in pipe_dict[tunnel[y][x]]: # 연결부 맞는지 확인하기
                        visited[y][x] = visited[r][c] + 1
                        if visited[y][x] <= L:
                            possibles += 1
                        else:
                            return possibles
                        q.append((x, y))       

    return possibles             


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M, R, C, L = map(int, input().split())

        tunnel = [list(map(int, input().split())) for _ in range(N)]
        visited = [[0 for _ in range(M)]for _ in range(N)]
        ans = BFS((C, R))

        print(f"#{tc} {ans}")

# git commit -m "code: Solve swea 1953 탈주범 검거 (yoonbaek)"