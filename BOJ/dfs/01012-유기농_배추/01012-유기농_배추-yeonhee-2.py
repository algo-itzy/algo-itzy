# BFS
# 인프런 - 파이썬 알고리즘 문제풀이 중 '섬나라 아일랜드' 강의 참고했습니다.

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    graph[y][x] = 0

    while Q:
        tmp = Q.popleft()
        for i in range(4):
            nx, ny =tmp[0]+dx[i], tmp[1]+dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx]:
                graph[ny][nx]=0
                Q.append((nx,ny))

for _ in range(int(input())):
    M, N, K = map(int, input().split())

    # 배추밭, 지렁이 수 초기화
    graph = [[0] * M for _ in range(N)]
    cnt = 0

    # 배추 정보 입력받기
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for y in range(N):
        for x in range(M):
            if graph[y][x]:  # 배추가 있으면
                # 모든 배추구역 탐색 후 카운트 1 증가
                bfs(x, y)
                cnt += 1

    print(cnt)
