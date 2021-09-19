# 1. 3개의 벽을 어떻게 쌓을지 <- n, m 의 값이 작아서 브루트 포스를 이용 <- 조
# 2. 벽을 다 쌓았으면, 바이러스를 전파시킴
# 3. 바이러스의 좌표를 하나씩 큐에 담아준 후, 탐색. 탐색이 끝나면 빈 칸의 개수를 체크해서 기존의 값보다 크면 교합체
# 3. 세운 벽을 허물고 벽을 쌓을 수 있는 다른 조합의 경우도 계산

# https://bgspro.tistory.com/18 이 블로그 보면서 따라 쳐봤는데, 답이 왜 다를까요... 못 찾겠네요..

from collections import deque
from itertools import combinations
import copy


def bfs():
    testgraph = copy.deepcopy(graph)
    queue = deque(virus)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= m:    # map 의 범위를 벗어나면 즉시 중단
                continue
            if testgraph[nx][ny] == 0:                    # 바이러스의 상하좌우가 0인 경우, 감염시키기
                testgraph[nx][ny] = 2
                queue.append((nx, ny))                    # 큐에 넣어 또 탐색
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:                          # 바이러스가 다 전파된 후 안전 영역의 갯수 구하기
                cnt += 1
    return cnt


n, m = map(int, input().split())
virus = []
empty = []

graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:                            # 바이러스 좌표 저장 리스트에 좌표 추가
            virus.append((i, j))
        elif graph[i][j] == 0:                          # 빈칸 좌표 저장 리스트에 좌표 추가
            empty.append((i, j))

dx = [0, 0, -1, 1]                                      # 상하좌우
dy = [1, -1, 0, 0]

ans = 0                                                 # 안전 영역의 최댓값을 담을 변수 ans
for data in combinations(empty, 3):                     # empty 리스트에서 3개를 선택하는 조합 (순서 고려 x)
    for x, y in data:
        graph[x][y] = 1                                 # 선택된 3개를 1로 바꿔 벽으로 만들어주고 bfs 실행
    ans = max(ans, bfs())                               # 기존 ans 와 bfs의 리턴값 중 더 큰 값을 ans 로
    for x, y in data:                                   # 선택했던 3개의 벽을 다시 0으로 만들어줘서 원래대로 복구시키기
        graph[x][y] = 0

print(ans)


# git commit -m "code: Solve boj 14502 연구소 (yeonju)"