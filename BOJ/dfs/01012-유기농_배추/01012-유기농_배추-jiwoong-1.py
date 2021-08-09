"""
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지
최소의 배추흰지렁이 마리 수
"""

# BFS
import sys

t = int(sys.stdin.readline())
x1 = [1, -1, 0, 0]
y1 = [0, 0, -1, 1]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for c in range(4):
            d = a + x1[c]
            e = b + y1[c]
            if 0 <= d < n and 0 <= e < m and f[d][e] == 1:
                f[d][e] = 0
                queue.append([d, e])


for i in range(t):
    m, n, k = map(int, input().split())
    f = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        f[b][a] = 1
    for d in range(n):
        for e in range(m):
            if f[d][e] == 1:
                bfs(d, e)
                f[d][e] = 0
                cnt += 1
    print(cnt)
