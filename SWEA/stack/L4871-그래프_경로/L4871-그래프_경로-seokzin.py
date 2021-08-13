def dfs(x):
    global res

    visit[x] = 1

    if x == G:
        res = 1
        return

    for nx in graph[x]:
        if not visit[nx]:
            dfs(nx)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    res = 0

    for i in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)

    S, G = map(int, input().split())

    dfs(S)

    print(f'#{tc} {res}')

# DFS의 return 처리는 어렵네요. 재귀를 벗어나면서 return이 계속 반복돼서..
# 그래서 global 변수를 어쩔 수 없이 썼습니다.