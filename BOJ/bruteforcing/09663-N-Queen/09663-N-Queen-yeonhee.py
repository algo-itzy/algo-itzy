import sys
input = sys.stdin.readline


def dfs(j):
    global cnt

    if j == N:
        cnt += 1
        return

    for i in range(N):
        if not (row[i] or right[j+i] or left[N-1+j-i]):
            row[i] = right[j+i] = left[N-1+j-i] = 1
            dfs(j+1)
            row[i] = right[j+i] = left[N-1+j-i] = 0


N = int(input())
cnt = 0

# 열 방향, 대각선 1, 대각선 2
row, right, left = [0]*N, [0]*(2*N-1), [0]*(2*N-1)

dfs(0)
print(cnt)
