# git commit -m "code: Solve swea L5249 최소 신장 트리 (jiwoong)"
def find_set(x):
    while x != edge[x]:
        x = edge[x]
    return x


def union(x, y):
    edge[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = list(range(V + 1))
    node = sorted([list(map(int, input().split())) for x in range(E)], key=lambda x: x[2])
    ans = 0
    for n1, n2, w in node:
        if find_set(n1) != find_set(n2):
            ans += w
            union(n1, n2)
    print('#{} {}'.format(tc, ans))
