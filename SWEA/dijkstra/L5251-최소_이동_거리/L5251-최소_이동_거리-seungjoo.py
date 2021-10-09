# git commit -m "code: Solve swea L5251 최소 이동 거리 (seungjoo)"
from heapq import heappush, heappop

def dijkstra(start):
    heap = []
    dists[start] = 0
    heappush(heap, (0, start))
    while heap:
        cur_dist, cur_node = heappop(heap)
        for next_node, next_dist in graph[cur_node]:
            dist = cur_dist + next_dist
            if dists[next_node] > dist:
                dists[next_node] = dist
                heappush(heap, (dist, next_node))


for test in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    graph = {i: [] for i in range(N + 1)}
    for __ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    dists = {i : float('inf') for i in range(N + 1)}

    dijkstra(0)
    
    print(f'#{test} {dists[N]}')