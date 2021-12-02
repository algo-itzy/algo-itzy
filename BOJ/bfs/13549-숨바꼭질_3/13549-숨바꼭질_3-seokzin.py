from collections import deque

LIMIT = 100001


def bfs():
    q = deque(([n]))

    while q:
        i = q.popleft()

    if i == k:
        return visit[i]

    for j in (i-1, i+1, i*2):
        if 0 <= j < LIMIT and not visit[j]:
            if j == i*2 and i != 0:
                visit[j] = visit[i] 
                q.appendleft(j)
            else:
                visit[j] = visit[i] + 1
                q.append(j)


n, k = map(int, input().split())
visit = [0] * LIMIT

print(bfs())