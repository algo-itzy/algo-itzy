# git commit -m "code: Solve swea 10966 물놀이를 가자 (jiwoong)"
from collections import deque


def bfs():
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    ans = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            dr = x + dxy[d][0]
            if dr < 0 or dr >= N:
                continue
            dc = y + dxy[d][1]
            if dc < 0 or dc >= M:
                continue
            if visited[dr][dc] != -1:
                continue

            visited[dr][dc] = visited[x][y] + 1
            ans += visited[dr][dc]
            q.append((dr, dc))
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        word = input()
        for j in range(M):
            if word[j] == 'W':
                visited[i][j] = 0
                q.append((i, j))
    print('#{} {}'.format(tc, bfs()))
