# git commit -m "code: Solve swea 1949 등산로 조성 (seungjoo)"
import sys
sys.stdin = open('input.txt')


def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and mountain[x][y] > mountain[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1)
            visited[nx][ny] = False


def new_start(candidates):
    for i, j in candidates:
        visited[i][j] = True
        dfs(i, j, 1)
        visited[i][j] = False


def make_climb_road():
    max_height = 0
    candidates = []
    for i in range(N):
        for j in range(N):
            if max_height < mountain[i][j]:
                max_height = mountain[i][j]
                candidates = [(i, j)]
            elif max_height == mountain[i][j]:
                candidates.append((i, j))
    for k in range(K + 1):
        for i in range(N):
            for j in range(N):
                if mountain[i][j] >= k:
                    mountain[i][j] -= k
                    new_start(candidates)
                    mountain[i][j] += k


for test in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    make_climb_road()
    print(f'#{test} {answer}')
