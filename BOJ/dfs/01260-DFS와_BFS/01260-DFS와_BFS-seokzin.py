from collections import deque

def dfs(v):
    print(v, end=' ')
    visit[v] = 1

    for i in range(1, n+1):  # 작은 점부터
        if not visit[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):        
    q = deque()
    q.append(v)

    visit[v] = 0

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if visit[i] and graph[v][i] == 1:
                q.append(i)
                visit[i] = 0


n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)  # 전역 스코프

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
    
dfs(v)
print()
bfs(v)

# visit 2개 쓰려했는데 visit를 뒤집어서 재활용하는 발상이 재밌어서 참고했습니다.
