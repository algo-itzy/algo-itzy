from collections import deque

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    s = list(map(int, input().split()))
    graph = [[] for _ in range(E+2)]  # E+1 노드까지 존재
    visit = [0] * (E+2)
    q = deque()

    for i in range(0, E*2, 2):
        graph[s[i]].append(s[i+1])

    # BFS
    q.append(N)
    visit[N] = 1

    while q:
        x = q.popleft()
        
        for nx in graph[x]:
            if not visit[nx]:
                q.append(nx)
                visit[nx] = 1

    print(f'#{tc}', sum(visit))

# BFS 약식으로 썼습니다.