# git commit -m "code: Solve swea L5248 그룹 나누기 (seungjoo)"
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    parents[y] = x


for test in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    prefer_set = list(map(int, input().split()))
    parents = {i: i for i in range(1, N + 1)}
    for i in range(M):
        a, b = prefer_set[i * 2], prefer_set[i * 2 + 1]
        if find(a) != find(b):
            union(a, b)
    group = set()
    for i in range(1, N + 1):
        if parents[i] not in group:
            x = find(i)
            if x not in group:
                group.add(x)
    print(f'#{test} {len(group)}')