import sys
from collections import deque

sys.stdin = open('input.txt')


def calculation(num, calc):
    if calc == 0:
        return num + 1
    elif calc == 1:
        return num - 1
    elif calc == 2:
        return num * 2
    elif calc == 3:
        return num - 10


def bfs(n, m):
    q = deque([(n, 0)])
    visited[n] = t

    while q:
        num, cnt = q.popleft()
        for i in range(4):
            num_next = calculation(num, i)
            if num_next == m:
                return cnt + 1
            elif 1 <= num_next <= 1000000 and visited[num_next] != t:
                q.append((num_next, cnt + 1))
                visited[num_next] = t


visited = [0] * 1000001
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{t} {bfs(N, M)}')
