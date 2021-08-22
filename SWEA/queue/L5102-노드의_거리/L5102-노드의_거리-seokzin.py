from collections import deque

def bfs():
    q.append((S, 0))
    visit[S] = 1

    while q:
        x, d = q.popleft()

        for nx in graph[x]:
            if not visit[nx]:
                q.append((nx, d+1))
                visit[nx] = 1

                if nx == G:
                    return d+1
    return 0

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visit = [0] * (v+1)
    q = deque()

    for i in range(e):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    S, G = map(int, input().split())

    print(f'#{tc}', bfs())

# q에 dis 값을 같이 저장시킨다.