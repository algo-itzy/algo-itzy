# git commit -m "code: Solve boj 13549 숨바꼭질 3 (jiwoong)"
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())


def bfs(n, k):
    num = 100001
    arr = [-1] * num
    arr[n] = 0
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(arr[x])
            break
        for i in (x * 2, x - 1, x + 1):
            if 0 <= i < num and arr[i] == -1:
                if i == 2 * x:
                    arr[i] = arr[x]
                    q.appendleft(i)
                else:
                    arr[i] = arr[x] + 1
                    q.append(i)
    return


bfs(N, K)
