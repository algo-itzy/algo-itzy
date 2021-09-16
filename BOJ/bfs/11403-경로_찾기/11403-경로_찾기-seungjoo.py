# git commit -m "code: Solve boj 11403 경로 찾기 (seungjoo)"
import sys
input = sys.stdin.readline

# 길이있고 안들렀으면 들러서 표시해줌.
def dfs(v):
    for u in range(n):
        if not visited[u] and matrix[v][u] == 1:
            visited[u] = 1
            dfs(i)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i)
    print(*visited)
