from sys import stdin
from collections import deque

rd = lambda : map(int, stdin.readline().split())


def BFS(start):
    q = deque([start])

    while q:
        now = q.popleft()

        for next in graph[now]:
            if next in jump:
                visited[next] = visited[now]+1
                next = jump[next]
            if not visited[next]:
                visited[next] = visited[now]+1
                q.append(next)
            if next == 100:
                return visited[next]


if __name__ == "__main__":
    N, M = rd()

    jump, graph = {}, {}
    visited = [0] * (100+1)

    for _ in range(N+M):
        start, end = rd()
        jump[start] = end

    for i in range(1, 100+1):
        if i not in graph:
            graph[i] = [i+n for n in range(1,7) if i+n <= 100]

    BFS(1)

    print(visited[100])

# git commit -m "code: Solve boj 16928 뱀과 사다리 게임 (yoonbaek)"