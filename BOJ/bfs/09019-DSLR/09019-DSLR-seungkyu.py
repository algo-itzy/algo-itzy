import sys
from collections import deque
# python으로는 통과가 안되네요


def bfs(num):
    queue = deque([(num, '')])
    visited[num] = 1

    while queue:
        num, reg = queue.popleft()
        if num == res:
            return reg

        # D
        n = (num*2)%10000
        if not visited[n]:
            visited[n] = 1
            queue.append((n, reg+'D'))
        # S
        n = (num-1)%10000
        if not visited[n]:
            visited[n] = 1
            queue.append((n, reg+'S'))
        
        # L
        n = num % 1000 * 10 + num // 1000
        if not visited[n]:
            visited[n] = 1
            queue.append((n, reg+'L'))
        # R
        n = num % 10 * 1000 + num // 10
        if not visited[n]:
            visited[n] = 1
            queue.append((n, reg+'R'))


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    visited = [0]*10000
    num, res = map(int, input().split())
    print(bfs(num))

# git commit -m "code: Solve boj 09019 DSLR (seungkyu)"