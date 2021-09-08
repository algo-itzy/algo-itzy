import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append([A, ''])  # 명령어를 같이 담음
    visited[A] = 1

    while q:
        x, y = q.popleft()
        if x == B:
            print(y)
        D = x * 2 % 10000  # 두 배 & 10000으로 나눈 나머지
        if not visited[D]:
            visited[D] = 1
            q.append([D, y+'D'])
        S = x - 1 if x != 0 else 9999  # n-1
        if not visited[S]:
            visited[S] = 1
            q.append([S, y + 'S'])
        L = x % 1000 * 10 + x // 1000  # 자리수를 왼편으로 회전
        if not visited[L]:
            visited[L] = 1
            q.append([L, y + 'L'])
        R = x % 10 * 1000 + x // 10  # 자리수를 오른편으로 회전
        if not visited[R]:
            visited[R] = 1
            q.append([R, y + 'R'])


for _ in range(int(input())):
    A, B = map(int, input().split())
    visited = [0] * 10000
    bfs()


"""
시간초과 때문에 PyPy3으로 제출했습니다.
"""
