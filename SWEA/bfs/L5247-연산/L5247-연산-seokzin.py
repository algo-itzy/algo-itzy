from collections import deque


def bfs():
    q = deque([(n, 0)])
    visit = [0] * 1000001

    while q:
        x, cnt = q.popleft()
        
        if x == m: 
            return cnt

        if visit[x]: 
            continue

        visit[x] = 1

        for nx in (x+1, x-1, x*2, x-10):
            if 0 < nx <= 1000000:
                q.append((nx, cnt+1))


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    print(f'#{tc}', bfs())