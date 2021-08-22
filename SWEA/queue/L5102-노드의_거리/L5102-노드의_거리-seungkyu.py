import sys
from collections import deque
sys.stdin = open('input5.txt')

def bfs():
    while queue: 
        start = queue.popleft()  # 시작점 업데이트
        for next in range(V+1):
            if nodes[start][next] and not dist[next]:
                dist[next] = dist[start] + 1  # 현재 지점 거리에서 거리 +1
                if next == G:
                    return dist[G]
                else:
                    queue.append(next)
    return 0

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    nodes = [[0] * (V+1) for _ in range(V+1)]  # 인접 행렬
    for _ in range(E): 
        a, b = map(int, input().split())
        nodes[a][b] = 1
        nodes[b][a] = 1
    S, G = map(int, input().split())
    queue = deque()
    queue.append(S)
    dist = [0] * (V+1) # 거리 저장
    print(f'#{test_case} {bfs()}')