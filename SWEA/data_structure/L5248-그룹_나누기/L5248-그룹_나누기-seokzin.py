def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])


def union(x,y):
    parent[find(y)] = find(x)


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    parent = list(range(n+1))
    arr = list(map(int, input().split()))

    for i in range(m):
        a, b = arr[2*i: 2*i+2]
        union(a, b)

    res = [find(i) for i in range(n+1)]
    
    print(f'#{tc}', len(set(res))-1)
