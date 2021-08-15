def dfs(start, end): 
    stack = []                         # 스택 초기화

    visited = [False] * (v+1)          # 방문 여부 검사할 행렬// 1~ v 까지 활용 
    stack.append(start)                # 시작점을 stack 에 삽입

    while stack:                       # stack 이 비기 전까지 반복 
        now = stack.pop()              # stack 의 마지막 값을 꺼냄 
        visited[now] = True

        for next in range(1, v+1):      
            if not visited[next] and node[now][next]: # 방문하지 않았고, 연결되어 있다면
                stack.append(next)      
        
    if visited[end]:                # 끝 점에 들린 적이 있다면
        return 1
    else: 
        return 0

t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split()) # 노드의 개수 v, 간선의 개수 e

    node = [[0] * (v+1) for _ in range(v+1)]

    for _ in range(e):                         # 간선의 개수만큼 연결된 거 1로 채워주기 (방향 ㅇ)
        start,  end = map(int,input().split()) # 출발, 도착 노드 (간선 정보)
        node[start][end] = 1
    s, g = map(int, input().split())  # 연결되어 있는지 확인할 노드 s, g

    print(f'#{tc} {dfs(s,g)}')


""""
3
---
6 5

1 4
1 3
2 3
2 5
4 6

1 6
----
7 4

1 6
2 3
2 6
3 5

2 5
----
9 9

2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8

1 9
"""