import sys
from heapq import heappop, heappush
from collections import defaultdict

sys.stdin = open('input.txt')


def dijkstra():
    heap = []
    heappush(heap, (0, 0))

    while heap:
        idx, w = heappop(heap)
        for nidx, nw in graph[idx]:
            tmp = w + nw
            if dist[nidx] > tmp:
                dist[nidx] = tmp
                heappush(heap, [nidx, tmp])


for t in range(1, int(input())+1):
    N, E = map(int, input().split())
    dist = [0] + [float('inf')]*N
    graph = defaultdict(list)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    dijkstra()
    print(f'#{t} {dist[N]}')
