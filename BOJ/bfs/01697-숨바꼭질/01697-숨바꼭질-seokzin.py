from collections import deque

LIMIT = 100001

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(visit[x])
            return

        for nx in (x-1, x+1, x*2):
            if 0 <= nx < LIMIT and not visit[nx]:
                visit[nx] = visit[x]+1
                q.append(nx)

n, k = map(int, input().split())
visit = [0] * LIMIT

bfs()

# 가장 빠른 시간 - BFS
# 풀고 다른 풀이들을 보니 다들 비슷하네요