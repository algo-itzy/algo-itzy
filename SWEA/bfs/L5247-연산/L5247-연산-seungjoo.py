# git commit -m "code: Solve swea L5247 연산 (seungjoo)"
from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = set()
    visited.add(start)
    while q:
        cur_node, cnt = q.popleft()
        for next_node in (cur_node + 1, cur_node - 1, cur_node * 2, cur_node - 10):
            if next_node <= int(1e6) and next_node not in visited:
                visited.add(next_node)
                q.append((next_node, cnt + 1))
                if next_node == M:
                    return cnt + 1


for test in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    print(f'#{test} {bfs(N)}')