import sys
input = sys.stdin.readline


def bellman_ford():
    dis[1] = 0
    for i in range(N):
        for v in range(1, N+1):
            for nv, nc in graph[v]:
                if dis[nv] > dis[v] + nc:
                    dis[nv] = dis[v] + nc
                    if i == N-1:
                        return 'YES'
    return 'NO'


for _ in range(int(input())):
    N, M, W = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    # float('inf') 쓰면 틀리게 나옴
    dis = [123456789] * (N+1)

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append([E, T])
        graph[E].append([S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append([E, -T])

    print(bellman_ford())
