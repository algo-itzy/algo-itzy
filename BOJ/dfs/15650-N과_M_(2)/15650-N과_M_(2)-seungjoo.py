# git commit -m "code: Solve boj 15650 N과 M (2) (seungjoo)"
import sys
input = sys.stdin.readline

def dfs(start, s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n + 1):
        if i not in s:
            dfs(i + 1, s + [i])

n, m = map(int, input().split())
dfs(1, [])