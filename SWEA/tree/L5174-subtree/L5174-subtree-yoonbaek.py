from collections import deque

intput = lambda : map(int, input().split())

def BFS(N):
    q = deque()
    q.append(N)
    visited[N] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            q.append(next)
            visited[next] = 1


if __name__ == "__main__":
    
    T = int(input())

    for tc in range(1, T+1):
        E, N = intput()
        edges = list(intput())

        graph = {i: [] for i in range(1, E+2)}
        visited = [0] * (E+2)

        # input
        for i in range(0, 2*E, 2):
            graph[edges[i]] += [edges[i+1]]

        BFS(N)

        print(f'#{tc} {sum(visited)}')
