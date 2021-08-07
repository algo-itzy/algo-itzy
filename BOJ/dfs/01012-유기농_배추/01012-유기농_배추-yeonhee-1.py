# DFS
# 파이썬 알고리즘 인터뷰 - 331p 섬의 개수 풀이 참고했습니다.
# 재귀 리밋...

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    # 더 이상 배추가 없는 경우 종료
    if x < 0 or x >= M or y < 0 or y >= N or graph[y][x] != 1:
        return
    
    # 탐색한 배추는 0으로 갱신
    graph[y][x] = 0

    # 동서남북 탐색
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

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
                dfs(x, y)
                # 모든 배추구역 탐색 후 카운트 1 증가
                cnt += 1

    print(cnt)
