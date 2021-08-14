import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V+1)]
    
    for _ in range(E):
        a, b = map(int, input().split())
        if b not in nodes[a]:
            nodes[a].append(b)  # 방향이 있으므로 a, b이면 nodes[a]에만 저장
    start, end = map(int, input().split())

    ans = 0
    while nodes[start]:  # 스택이 빌 때까지 진행
        node = nodes[start].pop()
        if node == end:  # 도착지 도달했으면 답은 1, break
            ans = 1
            break
        # 방문한 노드에 연결된 점들 모두 추가, 중복값은 제거
        nodes[start] = list(set(nodes[start] + nodes[node]))

    print(f'#{test_case} {ans}')