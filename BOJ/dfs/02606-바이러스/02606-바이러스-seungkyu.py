import sys
from collections import deque
input = sys.stdin.readline

pc = int(input())
n = int(input())

nodes = [[] for _ in range(pc+1)]  # 연결된 노드가 무엇인지 표시
visited = [0]*(pc+1)  # 방문 여부 표시 변수
queue = deque()  # bfs 이용하기 위한 deque

for _ in range(n):
    a, b = map(int, input().split())
    # a, b 연결된 것이면 b, a도 연결된 것이므로 2번 append 진행
    nodes[a].append(b)
    nodes[b].append(a)

ans = 0
# 시작점 1로 지정
queue.extend(nodes[1])
visited[1] = 1

while queue:
    num = queue.popleft()
    if not visited[num]:  # 방문하지 않은 점일 경우에 방문
        visited[num] = 1
        ans += 1
    for i in nodes[num]:  # deque에 넣을지 결정
        if not visited[i]:  # 방문하지 않은 점일 경우에만 append
            queue.append(i)
    
print(ans)
    