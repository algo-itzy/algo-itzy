import sys
sys.stdin = open('input.txt')


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])  # 경로 압축
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        x, y = y, x
    parents[y] = x


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    parents = list(range(V+1))  # 모든 원소를 대표자로 만듦

    graph = [list(map(int, input().split())) for _ in range(E)]
    graph.sort(key=lambda x: x[2])  # Kruskal : 가중치 순으로 정렬

    result = 0

    for n1, n2, w in graph:
        if find(n1) != find(n2):  # 싸이클이 발생하지 않는 경우
            union(n1, n2)
            result += w

    print(f'#{t} {result}')
