import sys
from _collections import deque

input = sys.stdin.readline


def check_range(i, j):
    return (0 <= i < N) and (0 <= j < N)


def bfs(node):
    q = deque()
    q.append(node)

    while q:
        n = q.popleft()
        for i in range(len(matrix[n])):
            if matrix[n][i] and arr[node][i] == 0:
                q.append(i)
                arr[node][i] = 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
arr = [[0 for _ in range(N)] for _ in range(N)]

for idx in range(N):
    bfs(idx)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()
