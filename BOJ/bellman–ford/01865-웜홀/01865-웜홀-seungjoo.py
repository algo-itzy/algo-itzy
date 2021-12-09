import sys
input = sys.stdin.readline

def bellman_ford(start):
    dists[start] = 0
    for cycle in range(n):
        for cur_node, next_node, cost in edges:
            if dists[cur_node] + cost < dists[next_node]:
                dists[next_node] = dists[cur_node] + cost
                if cycle == n - 1:
                    return True
    return False

INF = 123456789
for test in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    dists = {i: INF for i in range(1, n + 1)}
    
    print("YES" if bellman_ford(1) else "NO")