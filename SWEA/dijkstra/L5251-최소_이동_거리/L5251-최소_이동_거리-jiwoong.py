# git commit -m "code: Solve swea L5251 최소 이동 거리 (jiwoong)"
def dijkstra(s):
    visited[s] = 1
    dis = road[s]

    while 0 in visited:
        cnt, w = 0, 0
        for i in range(len(dis)):
            if not visited[i] and (cnt == 0 or dis[i] < cnt):
                cnt = dis[i]
                w = i
        visited[w] = 1
        for i in range(len(dis)):
            dis[i] = min(dis[i], dis[w] + road[w][i])
    return dis[-1]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    road = [[11] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        road[s][e] = w
    visited = [0] * (N + 1)

    print('#{} {}'.format(tc, dijkstra(0)))
