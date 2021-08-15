"""
# 그래프 경로
특정한 두 개의 노드에 경로가 존재하는지 확인
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력

첫 줄에 테스트 케이스 개수 T
테스트 케이스의 첫 줄에 V와 E
E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보
경로의 존재를 확인할 출발 노드 S와 도착노드 G

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
"""


def dfs(start):
    edge[start] = True
    ans = 0
    if start in node:  # 시작하는 노드가 있으면
        for next in node[start]:
            if not edge[next]:
                if next == G:
                    return 1  # 연결되어 있으면 1
                elif not ans:  # 아니면 계속 탐색
                    ans += dfs(next)  # S에서 G까지 계속
    return ans


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    node = {}
    edge = [False for _ in range(V + 1)]  # 노드에서 연결된 도착 노드의 리스트

    for _ in range(E):
        start, end = map(int, input().split())
        if start not in node:  # 시작노드에서 도착하는 노드의 리스트
            node[start] = [end]
        else:
            node[start].append(end)

    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S)}')