# git commit -m "code: Solve swea L5249 최소 신장 트리 (seungkyu)"
import sys
sys.stdin = open('input.txt')


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    parents[y] = x


def find(n):
    if parents[n] == n:
        return n
    else:
        parents[n] = find(parents[n])
        return parents[n]


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    parents = {i: i for i in range(V+1)}
    mat = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        mat.append((n1, n2, w))
    
    mat.sort(key=lambda x: x[2])
    cnt, tot = 0, 0

    for n1, n2, w in mat:
        if cnt == V:
            break
        if find(n1) != find(n2):
            union(n1, n2)
            cnt += 1
            tot += w

    print(f'#{tc} {tot}')
