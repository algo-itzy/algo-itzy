import heapq 

def dijkstra(start):
    pq = [start]
    while pq:
        now_dist, now = heapq.heappop(pq)

        if distances[now] < now_dist:
            continue
        for next, next_dist in graph[now]:
            next_dist += now_dist 
            if distances[next] > next_dist:
                distances[next] = next_dist
                heapq.heappush(pq, (next_dist, next))
            

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, E = map(int, input().split())
        distances = [0]+ [100000000] * (N)
        graph = [[] for _ in range(N+1)]

        for _ in range(E):
            s, e, w = map(int, input().split())
            graph[s].append((e,w))

        dijkstra((0, 0))
        
        print(f"#{tc} {distances[-1]}")
        
# git commit -m "code: Solve swea L5251 최소 이동 거리 (yoonbaek)"