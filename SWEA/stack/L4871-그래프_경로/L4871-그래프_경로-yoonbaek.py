# solved by YoonBaek

def graph_push(start: int, end: int):
    if not graph.get(start):
                graph[start] = [end]
    else:
        graph[start].append(end)


def dfs_stack(S: int):
    stack = []
    stack.append(S)

    while stack:
        now = stack.pop()

        if graph.get(now):
            for i in graph[now]:
                if not visited[i]:
                    visited[i] = 1
                    stack.append(i)
    

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        V, E = map(int, input().split())
        
        graph, visited = {}, [0] * (V+1)
        for _ in range(E):
            start, end = map(int, input().split())
            graph_push(start, end)

        S, G = map(int, input().split())

        dfs_stack(S)

        print(f"#{tc} {visited[G]}")
