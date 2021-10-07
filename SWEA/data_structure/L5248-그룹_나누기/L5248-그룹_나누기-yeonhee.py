import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x == parents[x]:  # 자신이 대표자
        return x
    return find_set(parents[x])  # 자신이 속한 집합의 대표자를 자신의 부모로


def union(x, y):  # 두 원소를 하나의 집합으로 합치기
    x = find_set(x)
    y = find_set(y)
    if x > y:
        x, y = y, x
    parents[y] = x


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # 모든 원소를 대표자로 만듦
    parents = list(range(N+1))

    for i in range(0, 2*M, 2):
        union(data[i], data[i+1])

    result = set()
    for i in range(len(parents)):
        result.add(find_set(i))

    print(f'#{t} {len(result)-1}')
