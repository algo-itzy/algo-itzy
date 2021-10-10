import heapq


def dijkstra(start):
    dp[start] = 0
    heap = []
    
    heapq.heappush(heap, [0, start])

    while heap:
        w, x = heapq.heappop(heap)

        for nx, nw in graph[x]:
            tmp = w + nw
            
            if tmp < dp[nx]:
                dp[nx] = tmp
                heapq.heappush(heap, [tmp, nx])


for tc in range(1, int(input())+1):
    n, e = map(int, input().split())

    graph = [[] for _ in range(e+1)] 
    dp = [float('inf')] * (e+1)

    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])

    dijkstra(0)

    print(f"#{tc}", dp[n])
