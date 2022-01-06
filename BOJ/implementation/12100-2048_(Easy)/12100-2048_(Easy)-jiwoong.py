# git commit -m "code: Solve boj 12100 2048 (Easy) (jiwoong)"
from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]


def rotate(B, N):
    deep = deepcopy(B)

    for i in range(N):
        for j in range(N):
            deep[j][N-i-1] = B[i][j]

    return deep


def convert(lst, N):
    lst = [i for i in lst if i]

    for i in range(1, len(lst)):
        if lst[i-1] == lst[i]:
            lst[i-1] *= 2
            lst[i] = 0

    lst = [i for i in lst if i]

    return lst + [0] * (N-len(lst))


def dfs(N, B, cnt):
    arr = max([max(i) for i in B])

    if cnt == 0:
        return arr

    for i in range(4):
        X = [convert(i, N) for i in B]

        if X != B:
            arr = max(arr, dfs(N, X, cnt-1))

        B = rotate(B, N)

    return arr


print(dfs(N, board, 5))