# git commit -m "code: Solve boj 21610 마법사 상어와 비바라기 (jiwoong)"
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    check = set()

    # 구름 이동
    for i, j in clouds:
        # 첫 행과 끝 행, 첫 열과 끝 열 연결
        nr, nc = (i + s * dr[d]) % N, (j + s * dc[d]) % N

        # 비 내려서 물 증가
        A[nr][nc] += 1

        # 구름 X
        check.add((nr, nc))

    # 물복사버그
    for i, j in check:
        # 대각선 거리 1 탐색
        for k in range(4):
            nr, nc = i + dr[2 + 2 * k], j + dc[2 + 2 * k]
            # 물 증가
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc]:
                A[i][j] += 1

    # 구름 생김
    clouds = []
    for r in range(N):
        for c in range(N):
            # 물 2 이상, 구름 O
            if A[r][c] > 1 and (r, c) not in check:
                clouds.append((r, c))  # 구름 생김
                A[r][c] -= 2  # 물 감소

print(sum(map(sum, A)))
