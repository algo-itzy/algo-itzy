import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = ((0, -1), (-1, 0), (0, 1))

N, M, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def target(tr, arr):  # 공격 가능한 적 위치 찾기
    if arr[N-1][tr]:  # target r
        return N-1, tr
    visited = [[0]*M for _ in range(N)]
    visited[N-1][tr] = 1
    q = deque([(N-1, tr)])
    dis = 1  # 궁수가 공격하는 거리
    while dis < D:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if -1 < nr < N and -1 < nc < M and not visited[nr][nc]:
                    if arr[nr][nc]:
                        return nr, nc
                    visited[nr][nc] = 1
                    q.append((nr, nc))
        dis += 1
    return -1, -1  # 공격 불가


def shoot(ac):  # 공격
    status = deque([row[:] for row in graph])  # 현재 격자판 상태
    kill = 0
    cnt = 0
    while cnt < N:
        enemy = [target(ac[i], status) for i in range(3)]
        for i in range(3):
            if enemy[i][0] < 0:  # 공격 불가
                continue
            if status[enemy[i][0]][enemy[i][1]]:
                kill += 1
                status[enemy[i][0]][enemy[i][1]] = 0
        status.pop()
        status.appendleft([0] * M)
        cnt += 1
    return kill


result = 0
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            kill = shoot([i, j, k])
            result = max(result, kill)
print(result)
