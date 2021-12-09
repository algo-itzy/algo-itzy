# git commit -m "code: Solve boj 01753 최단경로 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappush,heappop

def dijkstra(start):
    global min_dists
    heap = []
    min_dists = [float('INF')]*(V+1)
    min_dists[start] = 0
    heappush(heap,[min_dists[start],start])
    while heap:
        cur_dists,cur_node = heappop(heap)
        if cur_dists > min_dists[cur_node]:
            continue
        for next_dists,next_node in graph[cur_node]:
            dists = cur_dists + next_dists
            if dists < min_dists[next_node]:
                min_dists[next_node] = dists
                heappush(heap,[min_dists[next_node],next_node])
    return min_dists

V,E = map(int,input().split())
K = int(input())
graph = defaultdict(list)

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])

dijkstra(K)

for i in range(1,V+1):
    print(min_dists[i] if not min_dists[i] == float('inf') else 'INF')