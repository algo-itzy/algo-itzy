# solved by YoonBaek
# K를 찾기만 하면 되는게 아니라 최소 횟수를 찾아야 하기 때문에
# 깊이 들어가지 않고 상위 노드부터 찾는 BFS 알고리즘이 적절해 보입니다.
# 그리고 DFS 돌리면 무한 루프 돕니다

# 이 문제는 구현도 중요하지만 다음 위치를 노드와 연관시켜서
# BFS로 연결짓는 사고 방식이 중요한 거 같습니다
# BFS인걸 알고 푸니까 금방 풀었는데 모르고 풀었다면 한참 고민했을 듯

from collections import deque


def bfs(N: int, K: int):
    q.append(N)

    while q:
        now = q.popleft()

        if now == K:
            return visited[now]
        
        moves = [now-1, now+1, now*2]

        for move in moves:
            if 0 <= move <= MAX and not visited[move]:
                visited[move] = visited[now] + 1

                q.append(move)
        
        
if __name__ == "__main__":
    N, K = map(int, input().split())
    q, MAX = deque(), 100000
    
    visited = [0] * (MAX+1)

    print(bfs(N, K))
