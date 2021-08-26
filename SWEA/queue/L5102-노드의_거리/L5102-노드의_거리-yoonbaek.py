# DFS로 구현할 경우 쌍방향 그래프이기 때문에
# 반대편으로 돌아갔다가 찾을 수 있다고 생각 들어서
# 최단거리를 구할 때 사용하는 BFS로 구현해야겠다 생각

# edges를 어떻게 셀까...
# 1. pop할 때마다 세기: 갔다 온 곳도 세서 안됨
# 2. level 별로 distance 설정: 구현 어려워서 포기
# 3. 어차피 BFS는 한 번만 방문하니까 노드마다 하나의 이동거리만 가짐
#   -> 노드마다 이동거리를 달고 다니게 하자
#   -> append, pop을 똑같이 수행하는 dist(거리 큐) 구현

from collections import defaultdict, deque


def BFS(s, g: int):
    # q: 큐, q_dist: 이동거리 큐
    q = q_dist = deque()
    q.append(s); q_dist.append(0)
    visited[s] = 1

    while q:
        now = q.popleft()
        edges = q_dist.popleft()
        edges += 1

        for next in graphs[now]:
            if next == g:
                return edges
            if not visited[next]:
                visited[next] = 1
                q.append(next)
                q_dist.append(edges)

    return 0


inputs = lambda : map(int, input().split())


if __name__ == "__main__":
    T = int(input())
    
    for tc in range(1, T+1):
        V, E = inputs()

        graphs = defaultdict(list)
        visited = [0] * (V+1)

        for _ in range(E):
            L, R = inputs()
            graphs[L].append(R)
            graphs[R].append(L)

        S, G = inputs()

        edges = BFS(S, G)

        print(f"#{tc} {edges}")
    