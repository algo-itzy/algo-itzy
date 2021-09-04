import sys
from collections import deque


def bfs(x, y):
    queue = deque()
    dxdy = [(0, 1),(0, -1),(1, 0),(-1, 0)]

    # 시작점 queue에 넣고 방문 표시, cnt도 올려줌
    queue.append((x, y))
    cnt = 1
    matrix[x][y] = '0'

    while queue:
        x, y = queue.popleft()
        for i in dxdy:
            new_x = x + i[0]
            new_y = y + i[1]
            if 0<=new_x<N and 0<=new_y<N and matrix[new_x][new_y] == '1':
                # 새로 시작점 append, 방문 표시('0'으로 바꿈), cnt 증가
                queue.append((new_x, new_y))
                matrix[new_x][new_y] = '0'
                cnt += 1
    return cnt

input = sys.stdin.readline
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
ans = []

# matrix 돌면서 '1' 만날 때 진행
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1':
            ans.append(bfs(i, j))
            
# 답 sort후 출력
ans.sort()
print(len(ans))
print(*ans, sep='\n')
