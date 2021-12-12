# git commit -m "code: Solve boj 01865 웜홀 (seungkyu)"
import sys
input = sys.stdin.readline

def solution():
    dist[1] = 0
    for i in range(n):
        for v in range(1, n+1):
            for next, time in graph[v]:
                if dist[next] > dist[v] + time:
                    dist[next] = dist[v] + time

                    if i == n-1: 
                        return True
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    dist = [10001]*(n+1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    ans = solution()
    print('YES') if ans else print('NO')