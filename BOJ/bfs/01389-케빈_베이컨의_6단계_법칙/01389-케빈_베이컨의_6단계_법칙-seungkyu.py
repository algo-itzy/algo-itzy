import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

nodes = {i:[] for i in range(1, N+1)}  # dict로 연결노드 표시
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

def bfs(start):
    bacon = [0]*(N+1)  # start의 bacon수 구할 리스트
    visited[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        next = queue.popleft()
        for i in nodes[next]:
            if not visited[i]:
                bacon[i] = bacon[next] + 1
                visited[i] = 1
                queue.append(i)
    return sum(bacon)

result=[]
for num in range(1, N+1):  # 1번부터 N번까지 각자 베이컨 수 구함
    visited = [0]*(N+1)  # visited 매번 리셋
    result.append(bfs(num))

print(result.index(min(result)) + 1)
