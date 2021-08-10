from collections import deque


def bfs(n, k):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return time_cnt[x]

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not time_cnt[nx]:
                time_cnt[nx] = time_cnt[x] + 1
                q.append(nx)


n, k = map(int, input().split())
time_cnt = [0] * 100001

print(bfs(n, k))
