# DFS
import sys


def dfs(x, y):
    global cnt
    x1, y1 = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        x2, y2 = x + x1[i], y + y1[i]
        if x2 >= n or x2 < 0 or y2 >= m or y2 < 0 or worm[x2][y2]:
            continue
        if cabbage[x2][y2] != 0:
            worm[x2][y2] = 1
            dfs(x2, y2)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 5)
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        m, n, k = map(int, input().split())
        cabbage = [[0] * m for _ in range(n)]
        worm = [[0] * m for _ in range(n)]
        cnt = 0
        for _ in range(k):
            a, b = map(int, input().split())
            cabbage[b][a] = 1
        for i in range(n):
            for j in range(m):
                if cabbage[i][j] and not worm[i][j]:
                    worm[i][j] = 1
                    cnt += 1
                    dfs(i, j)
        print(cnt)
