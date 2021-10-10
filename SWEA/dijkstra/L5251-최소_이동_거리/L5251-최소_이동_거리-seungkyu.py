# git commit -m "code: Solve swea L5251 최소 이동 거리 (seungkyu)"
import sys
import heapq
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    dist = [float('inf') for _ in range(N+1)]
    node = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = list(map(int, input().split()))
        node[s].append((e, w))
    visited = [0]*(N+1)

    q = []
    heapq.heappush(q, (0, 0))

    while q:
        d, idx = heapq.heappop(q)
        if not visited[idx]:
            visited[idx] = 1
        
            for a, b in node[idx]:
                if dist[a] > d + b:
                    dist[a] = d + b
                    heapq.heappush(q, (dist[a], a))

    print(f'#{tc} {dist[N]}')
