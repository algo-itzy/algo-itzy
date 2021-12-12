import sys

input = sys.stdin.readline
INF = sys.maxsize


def bf():
    for i in range(n):
        for v in range(1, n+1):
            for nv, nw in graph[v]:
                if dis[nv] > dis[v] + nw:
                    dis[nv] = dis[v] + nw

                    if i == n-1:
                        return "YES"

    return "NO"


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    dis = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    print(bf())