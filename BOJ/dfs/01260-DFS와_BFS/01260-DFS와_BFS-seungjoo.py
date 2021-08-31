# git commit -m "code: Solve boj 01260 DFS와 BFS (seungjoo)"
import sys
input = sys.stdin.readline
from collections import defaultdict


def DFS(v):
    path.append(v)
    check[v] = True
    for i in graph[v]:
        if check[i]==False:
            DFS(i)


def BFS(v):
    queue = [v]
    path.append(v)
    check[v] = True
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if check[i] ==False:
                queue.append(i)
                path.append(i)
                check[i] = True


N,M,V = list(map(int,input().split()))
graph = defaultdict(list)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

for i in range(1,N+1):
    graph[i].sort()

path = []
check = [True] +[False]*(N)
DFS(V)
print(*path)

check = [True] +[False]*(N)
path.clear()
BFS(V)
print(*path)