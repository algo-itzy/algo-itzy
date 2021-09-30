from collections import deque

moves = ((1, 0), (0, 1))

def search():
    q = deque([(0,0)])
    visited[0][0] = mat[0][0]

    while q:
        c, r = q.popleft()

        for x, y in moves:
            x += c; y += r
            if x < N and y < N:
                acc = visited[r][c] + mat[y][x]
                if acc < visited[y][x]:
                    visited[y][x] = visited[r][c] + mat[y][x]
                    q.append((y, x))


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        mat = [list(map(int, input().split())) for _ in range(N)]
        visited = [[300 for _ in range(N)] for _ in range(N)]

        search()

        print(f"#{tc} {visited[N-1][N-1]}")

# git commit -m "code: Solve swea L5188 최소합 (yoonbaek)"