# DFS와 BFS 탐색 결과 출력
# stack의 경우 reverse sorting해야할 거 같아 재귀적으로 풀었습니다.
from collections import defaultdict, deque

ints = lambda : map(int, input().split())

def DFS(start):
    visited[start] = 1

    dfs.append(start)

    for next in graph[start]:
        if not visited[next]:
            visited[next] = 1
            DFS(next)


def BFS(start):
    q = deque([start])
    visited[start] = 0

    while q:
        now = q.popleft()
        bfs.append(now)

        for next in graph[now]:
            if visited[next]:
                visited[next] = 0
                q.append(next)


if __name__ == "__main__":
    nodes, edges, start = ints()
    graph = defaultdict(list)
    visited = [0] * (nodes+1)
    dfs, bfs = [], []

    for _ in range(edges):
        s, e = ints()
        graph[s].append(e)
        graph[e].append(s)
    
    for key in graph:
        graph[key].sort()

    DFS(start)
    BFS(start)

    print(*dfs)
    print(*bfs)
# git commit -m "code: Solve boj 01260 DFS와 BFS (yoonbaek)"