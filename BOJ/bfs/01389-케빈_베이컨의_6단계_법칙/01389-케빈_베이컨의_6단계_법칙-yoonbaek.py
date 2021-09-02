from sys import stdin
from collections import deque

read = stdin.readline
ints = lambda : map(int, read().split())

# 그냥 혹시 나중에 defaultdict 못 쓸 상황이 올 때 대비용 연습
class DefaultDict(dict):
    def __init__(self, type):
        self.type = type

    def push(self, key, val):
        if self.type == list:
            if key not in self:
                self[key] =[val]
            else:
                self[key].append(val)

# BFS로 각 start(사람)별 kevin bacon 거리를 구합니다.
def BFS(start, visited)->int:
    q = deque([start])

    while q:
        now = q.popleft()

        for next in graph[now]:
            if not visited[next]:
                # 다음 사람은 지금 사람보다 한 단계 더 걸칩니다.
                visited[next] = visited[now]+1
                q.append(next)


def get_kevin_bacon_cnt(start):
    kevin_bacon_cnt = 0

    visited = [0] * (N+1)
    BFS(start, visited)

    for i in range(1, N+1):
        # 본인을 제외한 케빈 베이컨 거리의 합을 구합니다.
        if i != start:
            kevin_bacon_cnt += visited[i]

    return kevin_bacon_cnt


if __name__ == "__main__":
    N, M = ints()
    graph = DefaultDict(list)
    
    for _ in range(M):
        A, B = ints()
        graph.push(A, B)
        graph.push(B, A)
    
    # 최소 초기값은 최대 6단계를 넘지 않으므로 6*N으로 설정합니다.
    min_kevin_bacon_cnt = 6*N

    # 각 사람을 돌며 최소값 업데이트
    for i in range(1, N+1):
        kbc = get_kevin_bacon_cnt(i)
        if kbc < min_kevin_bacon_cnt:
            min_kevin_bacon_cnt = kbc
            min_idx = i

    # 업데이트 결과 최소인 사람(idx) 출력
    print(min_idx)


# git commit -m "code: Solve boj 01389 케빈 베이컨의 6단계 법칙 (yoonbaek)"