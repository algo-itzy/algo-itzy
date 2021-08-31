
import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if level[a] >= level[b]:
        parent[b] = a
        if level[a]==level[b]:
            level[a] += 1
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = {i: i for i in range(1,N+1)}
level = {i:0 for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a,b)
cnt = set()
for i in range(1,N+1):
    pa = find(i)
    if pa not in cnt:
        cnt.add(pa)
print(len(cnt))