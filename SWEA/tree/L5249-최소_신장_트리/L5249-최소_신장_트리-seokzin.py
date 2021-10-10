def union(a, b):  # 사이클 검토
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


def find(a):  # 간선들이 이은 두 정점 찾기
    if a == parent[a]:
        return a

    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]


for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = []
    parent = list(range(v+1))
    res = 0

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))

    graph.sort()

    for w, s, e in graph:
        if find(s) != find(e):
            union(s, e)
            res += w

    print(f"#{tc}", res)
