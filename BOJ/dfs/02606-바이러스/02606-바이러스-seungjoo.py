import sys
input = sys.stdin.readline

# disjoint-set 서로소집합 union-find알고리즘.
# union은 원소 a,b가 속해있는 서로소 집합을 대푯값으로 묶어 표시한다.
def union(a,b):
    a=find(a)
    b=find(b)

    if level[a] >= level[b]:
        parent[b] = a
        level[a] += 1
    else:
        parent[a] = b
        level[b] += 1

# find는 각 집합의 대푯값(tree로 치면 root node)를 추적하는 함수.
def find(x):
    if x==parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

N = int(input())
M = int(input())
parent = {i:i for i in range(1,N+1)}
level = {i:1 for i in range(1,N+1)}
# a,b가 속해있는 집합이 다르면?(root node가 다르면?) 
# union연산을 통해 집합을 합친다.
for _ in range(M):
    a,b = map(int,input().split())
    if find(a) != find(b):
        union(a,b)

# 1번 노드와 연결되어있는 컴퓨터의 갯수를 세준다.
cnt=0
for computer in range(2,N+1):
    if find(1)==find(computer):
        cnt+=1

print(cnt)