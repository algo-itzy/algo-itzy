# git commit -m "code: Solve boj 11403 경로 찾기 (seungjoo)"
import sys
input = sys.stdin.readline

def dfs(v):
    for i in range(n):
        if visited[i] == 0 and matrix[v][i] == 1:
            visited[i] = 1
            dfs(i)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i)
    print(*visited)
