from collections import deque
import sys

input = sys.stdin.readline


def bfs(A, B):
    q = deque()
    q.append([A, ''])
    while q:
        num, ans = q.popleft()

        if num == B:
            print(ans)
            break

        d = (num * 2) % 10000
        if arr[d] == 0:
            arr[d] = 1
            q.append([d, ans + 'D'])

        s = num - 1 if num != 0 else 9999
        if arr[s] == 0:
            arr[s] = 1
            q.append([s, ans + 'S'])

        l = num % 1000 * 10 + num // 1000
        if arr[l] == 0:
            arr[l] = 1
            q.append([l, ans + 'L'])

        r = num % 10 * 1000 + num // 10
        if arr[r] == 0:
            arr[r] = 1
            q.append([r, ans + 'R'])


T = int(input())
for _ in range(T):
    arr = [0] * 10001
    A, B = map(int, input().split())
    bfs(A, B)
